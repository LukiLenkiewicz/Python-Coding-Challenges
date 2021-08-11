class Menu:
    LOGIN = 'login'
    HELP = 'help'
    EXIT = 'exit'
    ESC = 'esc'

    def menu(self):
        user_command = ''
        while user_command != self.EXIT:
            user_command = input(f'"{self.LOGIN}" otwiera menu logowania\n"{self.HELP}" wyświetla pomoc\n"{self.EXIT}" '
                                 f'opuszcza program\n')
            if user_command == self.LOGIN:
                self.login()
            elif user_command == self.HELP:
                self.help_interface()
            elif user_command == self.EXIT:
                pass
            else:
                print("Niepoprawna komenda użytkownika")

    def login(self):
        user_name = input('Podaj dane logowania lub wpisz "esc aby wyjść: ')
        if user_name != self.ESC:
            print(f"Witaj {user_name}")
        self.menu()

    def help_interface(self):
        print("Et Joseph dixit ad eum: Inserere haeret in asinum et adolebit. Dominici dixit: Insanis! Melius aditus ad"
              " calida aqua. Et Joseph dixit ad eum: Elegantia Gallia. Ex Epistola ad Corinthos: submota olivarum! Amen")
        while True:
            user_command = input('wpisz "esc" aby wyjść ')
            if user_command == self.ESC:
                self.menu()
            else:
                print('Niepoprawna komenda użytkownika.')


obj = Menu()
obj.menu()
