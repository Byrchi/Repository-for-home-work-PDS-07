import hashlib
import sys

def main():
    # Виводимо повідомлення вітання
    print("Вітаємо Вас на нашому ресурсі \n  ")
    while True:
        # Запитуємо у користувача, що він хоче зробити: увійти або зареєструватися
        print('Щоб залогуватися введіть "Login"\nЩоб створити аккаунт введіть "Signin"')
        n = input('Enter your message:')
        if n == "Login" or n == "Signin":
            if n == "Login":
                log_in()
            elif n == "Signin":
                sign_in()
        else:
            print('Повторіть спробу.')

def log_in():
    # Запитуємо у користувача email та пароль
    user_email = input('Введіть ваш email: ')
    user_password = input('Введіть ваш пароль: ')
    # Хешуємо пароль користувача
    hash_user_password = hash_password(user_password)

    # Відкриваємо файл з даними користувачів
    with open('users_data', 'r') as file:
        users_data = [line.strip().split(':') for line in file]

    # Перевіряємо, чи існує користувач з таким email та паролем
    for email, hashed_password in users_data:
        if user_email == email and hash_user_password == hashed_password:
            print("Успішний вхід.")
            sys.exit(0)
    else:
        print("Невірний email або пароль. Повторіть спробу.")

def sign_in():
    # Запитуємо у користувача email
    user_email = input('Введіть ваш емейл: ')
    # Перевіряємо, чи має email коректний формат
    if is_valid_email(user_email):
        # Відкриваємо файл з даними користувачів
        with open('users_data', 'r') as file:
            users_email = [line.split(':')[0] for line in file]

        # Перевіряємо, чи існує користувач з таким email
        if user_email in users_email:
            print("Даний емейл вже використовується. Повторіть спробу.")
            return

        # Запитуємо у користувача пароль
        user_password = input('Введіть ваш пароль: ')
        # Хешуємо пароль користувача
        hash_user_password = hash_password(user_password)
        # Зберігаємо дані користувача у файл
        with open('users_data', 'a+') as file:
            file.write(f"{user_email}:{hash_user_password}\n")
            print('Ви успішно створили аккаунт')
    else:
        print("Некоректний формат емейлу. Повторіть спробу.")

# Функція для хешування паролю
def hash_password(password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    return hashed_password

# Функція для перевірки формату email
def is_valid_email(email):
    return '@' in email

if __name__ == "__main__":
    main()
