import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 54000))
argument_a = input('Введіть перший аргумент "a" : ')
argument_b = input('Введіть другий аргумент "b" : ')
message = f"{argument_a} {argument_b}"
sock.send(bytes(message, encoding='UTF-8'))
data = sock.recv(1024)
sock.close()
print(data.decode("UTF-8"))