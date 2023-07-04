import socket



# sock.connect(('localhost', 55000))

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 55000))
    mesage = input('user:')
    sock.send(bytes(mesage, encoding='UTF-8'))
    response = sock.recv(1024).decode("UTF-8")
    print(f'server :{response}')
    if mesage == 'end':
        break
    sock.close()
