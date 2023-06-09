import socket

def chat_bot(response):
    if response == '1':
        return 'Hello world'
    if response == '2':
        return "Lorem in pussum"
    if response != '1' or '2':
        return "Unknow message, please enter the value 1 or 2 "


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55500))
sock.listen(15)
print ('Server is running')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    response = conn.recv(1024).decode("UTF-8")
    print(str(response))
    conn.send(bytes(chat_bot(response),encoding='UTF-8'))
conn.close()