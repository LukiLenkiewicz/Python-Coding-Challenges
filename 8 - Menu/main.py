LOGIN = 'login'
HELP = 'help'
EXIT = 'exit'
ESC = 'esc'


def menu():
    user_command = ''
    while user_command != EXIT:
        user_command = input('"login" otwiera menu logowania\n"help" wyświetla pomoc\n"exit"opuszcza program\n')
        if user_command == LOGIN:
            login()
        elif user_command == HELP:
            help_interface()
        elif user_command == EXIT:
            pass
        else:
            print("Niepoprawna komenda użytkownika")


def login():
    user_name = input('Podaj dane logowania lub wpisz "esc aby wyjść: ')
    if user_name != ESC:
        print(f"Witaj {user_name}")
    menu()


def help_interface():
    print("Et Joseph dixit ad eum: Inserere haeret in asinum et adolebit. Dominici dixit: Insanis! Melius aditus ad"
          " calida aqua. Et Joseph dixit ad eum: Elegantia Gallia. Ex Epistola ad Corinthos: submota olivarum! Amen")
    while True:
        user_command = input('wpisz "esc" aby wyjść ')
        if user_command == ESC:
            menu()
        else:
            print('Niepoprawna komenda użytkownika.')


menu()
