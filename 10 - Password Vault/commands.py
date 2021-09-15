class Commands:
    def __init__(self):
        self.ADD_WEBSITE = "add"
        self.GENERATE_PASSWORD = "generate"
        self.GET_PASSWORD = "get"
        self.GET_ACCOUNTS = "accounts"
        self.SAVE_PASSWORD = "save"
        self.REGENERATE_PASSWORD = "regenerate"
        self.DELETE_PASSWORD = "delete"
        self.GET_HELP = "help"
        self.USER_EXIT_COMMAND = "exit"
        self.HELP_COMMAND_CONTENT = f'"{self.ADD_WEBSITE}" <nazwa strony> dodaje nową stronę\n"{self.GENERATE_PASSWORD}"' \
                                    f'"{self.GENERATE_PASSWORD}" <nazwa strony> generuje hasło dla danej strony\n' \
                                    f'"{self.GET_PASSWORD}" <nazwa strony> zwraca hasło dla konkretnej strony\n' \
                                    f'"{self.GET_ACCOUNTS}" zwraca nazwy wszystkich stron dla których zostało ' \
                                    f'zapisane hasło\n"{self.SAVE_PASSWORD}" <nazwa strony> zapisuje manualnie stworzone ' \
                                    f'hasło dla konktretnej strony\n"{self.REGENERATE_PASSWORD}" tworzy nowe hasło\n' \
                                    f'"{self.DELETE_PASSWORD}" <nazwa strony> usuwa konto'\
                                    f'"{self.USER_EXIT_COMMAND}" opuszcza program'
