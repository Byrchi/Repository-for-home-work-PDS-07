import socket


while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 55500))
    message = input('user : ')
    sock.send(bytes(message, encoding='UTF-8'))
    response = sock.recv(1024).decode("UTF-8")
    print(f'server : {response}')
    if message == 'end session':
        break
    sock.close()
