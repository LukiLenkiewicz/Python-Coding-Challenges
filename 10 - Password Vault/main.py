import string
import sys
from random import randint
import commands
import file_handler
from constants import MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH


class PasswordVault:
    def __init__(self):
        file_handler.user_login()
        self.passwords = file_handler.create_new_file()
        self.f = file_handler.get_key()

    def user_interface(self):
        while True:
            user_command, user_website = self.input_user_data()
            self.check_user_command(user_command, user_website)
            file_handler.save_passwords(self.passwords)

    def input_user_data(self):
        user_input = input('Podaj komendę użytkownika lub wpisz "help" aby uzyskać pomoc: ')
        user_input = user_input.lower()
        user_input_list = user_input.split()
        user_command = user_input_list[0]
        try:
            user_website = user_input_list[1]
        except IndexError:
            user_website = None
        return user_command, user_website

    def check_user_command(self, command, website):
        if command == commands.GENERATE_PASSWORD:
            if website is None:
                print(f"Wygenerowane hasło {self.decrypt_password(self.generate_password())}")
            else:
                self.add_new_website(website)
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
            print(commands.HELP_COMMAND_CONTENT)
        elif command == commands.USER_EXIT_COMMAND:
            sys.exit()
        else:
            print("Niepoprawna komenda")

    def encrypt_password(self, password):
        password = self.f.encrypt(password.encode())
        return password.decode()

    def decrypt_password(self, password):
        password = self.f.decrypt(password.encode())
        return password.decode()

    def add_new_website(self, new_website):
        if new_website in self.passwords:
            print("Strona już została dodana")
        elif new_website is None:
            print("Musisz podać nazwę strony")
        else:
            self.passwords[new_website] = None
            print("Strona dodana z powodzeniem")

    def get_saved_password(self, name):
        if name in self.passwords.keys():
            if self.passwords[name] is None:
                print(f"Hasło do strony {name} nie zostało jeszcze dodane")
            else:
                word = self.decrypt_password(self.passwords[name])
                print(f"Hasło dla {name}: {word}")
        else:
            print("Taka strona nie została dodana.")

    def get_all_accounts(self):
        if len(self.passwords) > 0:
            print(f"Znaleziono {len(self.passwords)} przechowywanych kont:")
            for website in self.passwords.keys():
                print(f"-{website}")
        else:
            print("Nie dodano jeszcze żadnych kont.")

    def generate_website_password(self, name):
        if name in self.passwords.keys():
            if self.passwords[name] is None:
                self.passwords[name] = self.generate_password()
                print("Hasło zostało wprowadzone")
            else:
                print('Hasło zostało już dodane, użyj komendy "regenerate" aby je zmienić')
        else:
            print("Taka strona nie została jeszcze dodana")

    def generate_password(self):
        n = randint(MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH)
        elements = list(string.ascii_letters + string.digits + string.punctuation)
        password = ""
        for i in range(n):
            password += elements[randint(0, len(elements) - 1)]
        password = self.encrypt_password(password)
        return password

    def regenerate_password(self, website):
        if not website:
            print("Musisz podać nazwę jakiejś strony")
        elif website in list(self.passwords.keys()):
            if self.passwords[website] is not None:
                self.passwords[website] = self.generate_password()
                print("Hasło zostało zmienione")
            elif self.passwords[website] is None:
                print("Hasło do tej strony nie zostało jeszcze dodane")
        else:
            print("Taka strona nie została dodana")

    def save_password(self, name):
        if name in self.passwords.keys():
            new_password = input("Podaj hasło, które chcesz wprowadzić: ")
            self.passwords[name] = self.encrypt_password(new_password)
            print("Hasło zostało wprowadzone")
        else:
            print("Taka strona nie istnieje")

    def delete_password(self, website):
        if website in list(self.passwords.keys()):
            del self.passwords[website]
            print(f'Strona "{website}" została usunięta')
        else:
            print("Taka strona nie została dodana")


obj = PasswordVault()
obj.user_interface()
