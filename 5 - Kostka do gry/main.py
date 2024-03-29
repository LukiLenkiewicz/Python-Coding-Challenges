from random import randint

MIN_NUM_OF_DOTS = 1
MAX_NUM_OF_DOTS = 6

MAX_NUM_OF_DICES = 4
MIN_NUM_OF_DICES = 1

CONTINUE_THE_GAME_COMMANDS = ['y', 'yes', 't', 'tak']
USER_EXIT_COMMANDS = ['n', 'no', 'nie']


def choose_number_of_dices():
    while True:
        number_of_throws = input("Masz 4 kości, iloma chcesz rzucić? ")
        if number_of_throws.isdigit():
            number_of_throws = int(number_of_throws)
            if number_of_throws > MAX_NUM_OF_DICES or number_of_throws < MIN_NUM_OF_DICES:
                print("Nieodpowiednia liczba kości. Spróbuj ponownie.")
            else:
                return int(number_of_throws)
        else:
            print("Podaj liczbę całkowitą.")


def continue_the_game():
    while True:
        answer = input(f"Czy chcesz grać dalej?\nWpisz {', '.join(CONTINUE_THE_GAME_COMMANDS)} aby kontynuować\nlub "
                       f"{', '.join(USER_EXIT_COMMANDS)} aby zakończyć.")
        if answer in CONTINUE_THE_GAME_COMMANDS:
            return True
        elif answer in USER_EXIT_COMMANDS:
            return False
        else:
            print("Podano nieprawidłową wartość, spróbuj ponownie.")


def throw():
    number_of_throws = choose_number_of_dices()
    game_on = True
    while game_on:
        result = randint(number_of_throws*MIN_NUM_OF_DOTS, number_of_throws*MAX_NUM_OF_DOTS)
        print(f"Uzyskana liczba oczek to: {result}")
        game_on = continue_the_game()


throw()
