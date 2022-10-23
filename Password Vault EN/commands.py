GENERATE_PASSWORD = "generate"
GET_PASSWORD = "get"
GET_ACCOUNTS = "accounts"
SAVE_PASSWORD = "save"
REGENERATE_PASSWORD = "regenerate"
DELETE_PASSWORD = "delete"
GET_HELP = "help"
USER_EXIT_COMMAND = "exit"
HELP_COMMAND_CONTENT = f'"{GENERATE_PASSWORD}" <website name> adds new webiste and generates ' \
                       f'password for it\n"{GENERATE_PASSWORD}" generates new password\n' \
                       f'"{GET_PASSWORD}" <website name> returns password for given website\n' \
                       f'"{GET_ACCOUNTS}" returns names of all websites for which password' \
                       f'has been saved\n"{SAVE_PASSWORD}" <website name> saves manually' \
                       f' password created for given website\n"{REGENERATE_PASSWORD}" ' \
                       f'<website name> creates new password\n"{DELETE_PASSWORD}" ' \
                       f'<website name> removes account\n"{USER_EXIT_COMMAND}" leaves program'