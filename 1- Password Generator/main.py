import string
from random import randint


def password_generator(n):
    elements = list(string.ascii_letters + string.digits + string.punctuation)
    password = ''
    for i in range(n):
        password += elements[randint(0, len(elements) - 1)]
    return password


n = 0

while n < 8 or n > 40:
    n = int(input("Podaj długość hasła: "))
    if n < 8 or n > 40:
        print("Hasło powinno zawierać od 8 do 40 znaków, spróbuj ponownie")

print(password_generator(n))
