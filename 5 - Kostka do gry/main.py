from random import randint

MIN_NUM_OF_DOTS = 1
MAX_NUM_OF_DOTS = 6

CONTINUE_THE_GAME = ['y', 'yes', 't', 'tak']
STOP_THE_GAME = ['n', 'no', 'nie']

MAX_NUM_OF_DICES = 4
MIN_NUM_OF_DICES = 1


def choose_number_of_dices():
    number_of_throws = int(input("Masz 4 kości, iloma chcesz rzucić? "))

    while number_of_throws > MAX_NUM_OF_DICES or number_of_throws < MIN_NUM_OF_DICES:
        number_of_throws = int(input("Nieodpowiednia liczba kości. Spróbuj ponownie: "))

    return number_of_throws


def throw():

    number_of_throws = choose_number_of_dices()

    while True:
        result = randint(number_of_throws*MIN_NUM_OF_DOTS, number_of_throws*MAX_NUM_OF_DOTS)
        print(f"Uzyskana liczba oczek to: {result}")

        continue_game = input("Czy chcesz grać dalej? ")

        if continue_game in CONTINUE_THE_GAME:
            continue
        elif continue_game in STOP_THE_GAME:

            break


throw()
