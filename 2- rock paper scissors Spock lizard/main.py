from random import choice

MOVES = ["Paper", "Rock", "Scissors", "Spock", "Lizard"]

BEATS = {
    "Paper": ["Rock", "Spock"],
    "Rock": ["Scissors", "Lizard"],
    "Scissors": ["Paper", "Lizard"],
    "Spock": ["Rock", "Scissors"],
    "Lizard": ["Paper", "Spock"]
}


def player_turn():
    player_move = input()
    player_move = player_move.capitalize()

    while player_move not in MOVES and player_move != "Stop":
        print("Zły ruch, spróbuj ponownie: ")
        player_move = input()
        player_move = player_move.capitalize()

    return player_move


def gameplay():

    player_points = 0
    computer_points = 0

    while True:
        for move in MOVES:
            print(move, end='\t')
        print('\nWybierz jedną z powyższych figur lub wpisz "Stop" aby zakończyć: ')

        player_move = player_turn()
        computer_move = choice(MOVES)
        if player_move == "Stop":
            break

        if computer_move in BEATS[player_move]:
            player_points += 1
            print(f"{player_move} beats {computer_move}")
        elif player_move in BEATS[computer_move]:
            computer_points += 1
            print(f"{computer_move} beats {player_move}")
        else:
            print("Remis")

        print(f"Punkty gracza: {player_points}\nPunkty komputera: {computer_points}\n")


gameplay()
