import string
import sys
from random import randint
import commands
import file_handler
from constants import MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH


class PasswordVault:
    def __init__(self):
        file_handler.user_login()
        self.passwords = file_handler.get_passwords()
        self.f = file_handler.get_key()

    def user_interface(self):
        while True:
            user_command, user_website = self.input_user_data()
            self.check_user_command(user_command, user_website)
            file_handler.save_passwords(self.passwords)

    def input_user_data(self):
        user_input = input('Pass user command or type "help" to get help: ')
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
                print(f"Generated password: {self.decrypt_password(self.generate_password())}")
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
            print("Incorrect command")

    def encrypt_password(self, password):
        password = self.f.encrypt(password.encode())
        return password.decode()

    def decrypt_password(self, password):
        password = self.f.decrypt(password.encode())
        return password.decode()

    def add_new_website(self, new_website):
        if new_website in self.passwords:
            print("The website has been already added")
        elif new_website is None:
            print("You must enter the website name")
        else:
            self.passwords[new_website] = None
            print("Website added successfully")

    def get_saved_password(self, name):
        if name in self.passwords.keys():
            if self.passwords[name] is None:
                print(f"Password to the website {name} has not been added yet")
            else:
                word = self.decrypt_password(self.passwords[name])
                print(f"{name}'s password: {word}")
        else:
            print("This website has not been added yet")

    def get_all_accounts(self):
        if len(self.passwords) > 0:
            print(f"{len(self.passwords)} stored accounts were found:")
            for website in self.passwords.keys():
                print(f"-{website}")
        else:
            print("No accounts have been added yet")

    def generate_website_password(self, name):
        if name in self.passwords.keys():
            if self.passwords[name] is None:
                self.passwords[name] = self.generate_password()
                print("Password has been entered")
            else:
                print('Password has been already added. Use command "regenerate" to change it')
        else:
            print("This website has not been added yet")

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
            print("You must pass website's name")
        elif website in list(self.passwords.keys()):
            if self.passwords[website] is not None:
                self.passwords[website] = self.generate_password()
                print("Password has been changed")
            elif self.passwords[website] is None:
                print("Password to this website has not been added yet")
        else:
            print("This website has not been added yet")

    def save_password(self, name):
        if name in self.passwords.keys():
            new_password = input("Pass the password you want to add: ")
            self.passwords[name] = self.encrypt_password(new_password)
            print("Password has been added")
        else:
            print("This webiste doesn't exist")

    def delete_password(self, website):
        if website in list(self.passwords.keys()):
            del self.passwords[website]
            print(f'"{website}" has been removed')
        else:
            print("This website hasn't been added")


obj = PasswordVault()
obj.user_interface()
