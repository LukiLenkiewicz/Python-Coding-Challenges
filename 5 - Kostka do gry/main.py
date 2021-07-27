from random import randint

MIN_NUM_OF_DOTS = 1
MAX_NUM_OF_DOTS = 6

MAX_NUM_OF_DICES = 4
MIN_NUM_OF_DICES = 1

CONTINUE_THE_GAME = ['y', 'yes', 't', 'tak']
STOP_THE_GAME = ['n', 'no', 'nie']


def choose_number_of_dices():
    while True:
        number_of_throws = int(input("Masz 4 kości, iloma chcesz rzucić? "))
        if number_of_throws <= MAX_NUM_OF_DICES and number_of_throws >= MIN_NUM_OF_DICES:
            return number_of_throws
        else:
            print("Nieodpowiednia liczba kości. Spróbuj ponownie.")


def print_message():
    print("Czy chcesz grać dalej? ")
    print("Wpisz: ", end='')
    for word in CONTINUE_THE_GAME:
        print(f"{word}, ", end='')
    print("żeby kontynuować")
    print("Lub ", end='')
    for word in STOP_THE_GAME:
        print(f"{word}, ", end='')
    print("żeby zakończyć")
    return input()


def continue_the_game():
    while True:
        answer = print_message()
        if answer in CONTINUE_THE_GAME:
            return True
        elif answer in STOP_THE_GAME:
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
