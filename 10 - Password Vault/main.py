import json
import string
from random import randint
from commands import Commands


class PasswordVault:
    def __init__(self):
        self.JSON_FILE_NAME = "hidden.passwords.json"
        self.passwords = self.create_new_file()

    def user_interface(self):
        while True:
            user_input = input("Podaj komendę użytkownika: ")
            user_input = user_input.lower()
            user_input_list = user_input.split()
            user_command = user_input_list[0]
            try:
                user_website = user_input_list[1]
            except IndexError:
                user_website = None
            self.check_user_command(user_command, user_website)

    def check_user_command(self, command, website):
        commands = Commands()
        if command == commands.ADD_WEBSITE:
            self.add_new_website()
        elif command == commands.GENERATE_PASSWORD:
            if website is None:
                print(self.generate_password())
            else:
                self.generate_website_password(website)
        elif command == commands.GET_PASSWORD:
            self.get_saved_password(website)
        elif command == commands.GET_ACCOUNTS:
            self.get_all_accounts()
        elif command == commands.SAVE_PASSWORD:
            self.save_password(website)
        elif command == commands.REGENERATE_PASSWORD:
            self.regenerate_password(website)
        elif command == commands.DELETE_PASSWORD:
            self.delete_password(website)
        elif command == commands.GET_HELP:
            print(f"Sprawdź sobie plik commands bo nie chce mi się pisać")
        else:
            print("Niepoprawna komenda")

    def add_new_website(self):
        new_website = input("Podaj nazwę strony:")
        if new_website in self.passwords:
            print("Strona już została dodana")
        else:
            self.passwords[new_website] = ""

    def create_new_file(self):
        try:
            with open(self.JSON_FILE_NAME, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Tworzenie pustej listy haseł")
            passwords = {}
            with open(self.JSON_FILE_NAME, 'w') as file:
                json.dump(passwords, file)
            return passwords

    def get_saved_password(self, name):
        if name in self.passwords:
            print(f"Hasło dla {name}: {self.passwords[name]}")

    def get_all_accounts(self):
        print(f"Znaleziono {len(self.passwords)} przechowywanych kont:")
        for website in self.passwords.keys():
            print(f"-{website}")

    def generate_website_password(self, name):
        self.passwords[name] = self.generate_password()

    def generate_password(self):
        n = ''
        while not n.isdigit():
            n = input("Podaj długość hasła: ")
        n = int(n)
        elements = list(string.ascii_letters + string.digits + string.punctuation)
        password = ""
        for i in range(n):
            password += elements[randint(0, len(elements) - 1)]
        return password

    def regenerate_password(self, website):
        if website in list(self.passwords.keys()):
            self.passwords[website] = self.generate_password()
        else:
            print("Taka strona nie została dodana.")

    def save_password(self, name):
        self.passwords[name] = input("Podaj hasło do strony: ")

    def delete_password(self, website):
        if website in list(self.passwords.keys()):
            del self.passwords[website]
            print("Strona została usunięta")
        else:
            print("Taka strona nie została dodana")


obj = PasswordVault()
obj.user_interface()
