import string
from random import randint

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 40


def password_generator(n):
    elements = list(string.ascii_letters + string.digits + string.punctuation)
    password = ''
    for i in range(n):
        password += elements[randint(0, len(elements) - 1)]
    return password


def ask_about_password_length(password_length = 0):
    while password_length < MIN_PASSWORD_LENGTH or password_length > MAX_PASSWORD_LENGTH:
        password_length = int(input("Podaj długość hasła: "))
        if password_length < MIN_PASSWORD_LENGTH or password_length > MAX_PASSWORD_LENGTH:
            print("Hasło powinno zawierać od 8 do 40 znaków, spróbuj ponownie")

    return password_length


password_length = ask_about_password_length()
print(password_generator(password_length))
