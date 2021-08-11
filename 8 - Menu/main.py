LOGIN = 'login'
HELP = 'help'
EXIT = 'exit'
ESC = 'esc'


class Menu:
    def menu(self):
        user_command = ''
        while user_command != EXIT:
            user_command = input(f'"{LOGIN}" otwiera menu logowania\n"{HELP}" wyświetla pomoc\n"{EXIT}" opuszcza program\n')
            if user_command == LOGIN:
                self.login()
            elif user_command == HELP:
                self.help_interface()
            elif user_command == EXIT:
                pass
            else:
                print("Niepoprawna komenda użytkownika")

    def login(self):
        user_name = input('Podaj dane logowania lub wpisz "esc aby wyjść: ')
        if user_name != ESC:
            print(f"Witaj {user_name}")
        self.menu()

    def help_interface(self):
        print("Et Joseph dixit ad eum: Inserere haeret in asinum et adolebit. Dominici dixit: Insanis! Melius aditus ad"
              " calida aqua. Et Joseph dixit ad eum: Elegantia Gallia. Ex Epistola ad Corinthos: submota olivarum! Amen")
        while True:
            user_command = input('wpisz "esc" aby wyjść ')
            if user_command == ESC:
                self.menu()
            else:
                print('Niepoprawna komenda użytkownika.')


obj = Menu()
obj.menu()
