import json
from random import randint
import string


class PasswordVault:

    def get_saved_passwords(self):
        pass

    def generate_web_password(self):
        password = self.generate_password()

    def generate_password(self):
        n = input("Podaj długość hasła")
        elements = list(string.ascii_letters + string.digits + string.punctuation)
        password = ''
        for i in range(n):
            password += elements[randint(0, len(elements) - 1)]
        return password

