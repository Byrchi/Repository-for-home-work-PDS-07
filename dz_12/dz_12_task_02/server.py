import socket
import asyncio

send_data = []

async def addition(a, b):
    await asyncio.sleep(1)
    send_data.append(f'a + b = {a+b}\n')

async def subtraction(a, b):
    await asyncio.sleep(2)
    send_data.append(f'a - b = {a-b}\n')

async def multiplication(a, b):
    await asyncio.sleep(3)
    send_data.append(f'a * b = {a*b}\n')

def task():
    ioloop = asyncio.get_event_loop()
    tasks = [
        ioloop.create_task(addition(a, b)),
        ioloop.create_task(subtraction(a, b)),
        ioloop.create_task(multiplication(a, b))
    ]
    ioloop.run_until_complete(asyncio.wait(tasks))
    ioloop.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 54000))
sock.listen(10)
print ('Server is running, please, press ctrl+c to stop')

while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    a, b = data.decode("UTF-8").split(' ')
    a = int(a)
    b = int(b)
    task()
    print(send_data)
    answer = ' '.join(send_data).encode('UTF-8')

    conn.send(answer)
conn.close()