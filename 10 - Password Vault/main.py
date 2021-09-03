import json
from random import randint
import string


class PasswordVault:

    def __init__(self):
        self.JSON_FILE_NAME = 'hidden.passwords.json'
        self.passwords = self.create_new_file()

    def user_interface(self):
        while True:
            user_command = input("Podaj komendę użytkownika: ")

    def check_user_command(self, command):
        if command == "generate name":
            self.generate_web_password()
        elif command == "generate":
            print(self.generate_password())
        elif command == "get":
            self.get_all_accounts()


    def create_new_file(self):
        try:
            with open(self.JSON_FILE_NAME, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print('Tworzenie pustej listy zadań')
            passwords = {}
            with open(self.JSON_FILE_NAME, 'w') as file:
                json.dump(passwords, file)
            return passwords

    def get_saved_passwords(self):
        pass

    def get_all_accounts(self):
        print(f"Found {len(self.passwords)} stored accounts:")
        for website in self.passwords.keys():
            print(f"-{website}")

    def generate_web_password(self, name):
        password = self.generate_password()
        self.passwords[name] = password

    def generate_password(self):
        n = input("Podaj długość hasła")
        elements = list(string.ascii_letters + string.digits + string.punctuation)
        password = ''
        for i in range(n):
            password += elements[randint(0, len(elements) - 1)]
        return password


