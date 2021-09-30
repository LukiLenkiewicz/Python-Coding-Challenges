GENERATE_PASSWORD = "generate"
GET_PASSWORD = "get"
GET_ACCOUNTS = "accounts"
SAVE_PASSWORD = "save"
REGENERATE_PASSWORD = "regenerate"
DELETE_PASSWORD = "delete"
GET_HELP = "help"
USER_EXIT_COMMAND = "exit"
HELP_COMMAND_CONTENT = f'"{GENERATE_PASSWORD}" <nazwa strony> dodaje nową stronę i generuje dla' \
                       f'niej haslo\n"{GENERATE_PASSWORD}" generuje nowe haslo\n' \
                       f'"{GET_PASSWORD}" <nazwa strony> zwraca hasło dla konkretnej strony\n' \
                       f'"{GET_ACCOUNTS}" zwraca nazwy wszystkich stron dla których zostało ' \
                       f'zapisane hasło\n"{SAVE_PASSWORD}" <nazwa strony> zapisuje manualnie' \
                       f' stworzone hasło dla konktretnej strony\n"{REGENERATE_PASSWORD}" ' \
                       f'<nazwa strony> tworzy nowe hasło\n"{DELETE_PASSWORD}" ' \
                       f'<nazwa strony> usuwa konto\n"{USER_EXIT_COMMAND}" opuszcza program'
