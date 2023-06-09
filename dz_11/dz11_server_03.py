import socket

#Данну функцію додав до коду, оскільки текст від кієнта може прийти з знаками пунктуації.
# Дана функція очищує текст.

def clean_string(response):
    punctuation_marks = [',', '.', '!', '?', ';', ':', '-', '(', ')', '[', ']', '{', '}', "'", '"', "/", "\\", "_"]
    clean_text = ''
    for i in response:
        if i not in punctuation_marks:
            clean_text += i
    return clean_text

#Дана функція обраховує кулькість слів в тексті, поруч з тим після очищення тексту є можливість винекнення
# потрійного пробілу.Функція змінює подвійний пробіл на пустий знак, оскільки при підрахунку слів
# потрійний пробіл рахує як слово.

def quality_words_in_response():
    text_res = clean_string(response).replace('  ', ' ')
    return str(len(text_res.split(' ')))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55501))
sock.listen(15)

print ('Server is running')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    response = conn.recv(1024).decode("UTF-8")
    print(quality_words_in_response())
    conn.send(bytes(quality_words_in_response(), encoding="UTF-8"))
conn.close()
