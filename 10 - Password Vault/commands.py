class Commands:
    def __init__(self):
        self.GENERATE_PASSWORD = "generate"
        self.GET_PASSWORD = "get"
        self.GET_ACCOUNTS = "accounts"
        self.SAVE_PASSWORD = "save"
        self.REGENERATE_PASSWORD = "regenerate"
        self.DELETE_PASSWORD = "delete"
        self.GET_HELP = "help"
        self.USER_EXIT_COMMAND = "exit"
        self.HELP_COMMAND_CONTENT = f'"{self.GENERATE_PASSWORD}" <nazwa strony> dodaje nową stronę i generuje dla' \
                                    f'niej haslo\n"{self.GENERATE_PASSWORD}" tworzy generuje nowe haslo\n' \
                                    f'"{self.GENERATE_PASSWORD}" tworzy generuje nowe haslo\n' \
                                    f'"{self.GET_PASSWORD}" <nazwa strony> zwraca hasło dla konkretnej strony\n' \
                                    f'"{self.GET_ACCOUNTS}" zwraca nazwy wszystkich stron dla których zostało ' \
                                    f'zapisane hasło\n"{self.SAVE_PASSWORD}" <nazwa strony> zapisuje manualnie' \
                                    f' stworzone hasło dla konktretnej strony\n"{self.REGENERATE_PASSWORD}"' \
                                    f'tworzy nowe hasło\n"{self.DELETE_PASSWORD}" <nazwa strony> usuwa konto' \
                                    f'"{self.USER_EXIT_COMMAND}" opuszcza program'
