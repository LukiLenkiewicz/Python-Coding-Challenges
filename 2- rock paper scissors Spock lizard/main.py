from random import choice

BEATS = {
    "Paper": ["Rock", "Spock"],
    "Rock": ["Scissors", "Lizard"],
    "Scissors": ["Paper", "Lizard"],
    "Spock": ["Rock", "Scissors"],
    "Lizard": ["Paper", "Spock"]
}

MOVES = list(BEATS.keys())

USER_EXIT_COMMAND = "Stop"


def player_turn():
    player_move = input()
    player_move = player_move.capitalize()

    while player_move not in MOVES and player_move != USER_EXIT_COMMAND:
        print("Zły ruch, spróbuj ponownie: ")
        player_move = input()
        player_move = player_move.capitalize()

    return player_move


def compare_moves(player_move, computer_move, player_points, computer_points):
    if computer_move in BEATS[player_move]:
        print(f"{player_move} beats {computer_move}")
        return player_points + 1, computer_points

    elif player_move in BEATS[computer_move]:
        print(f"{computer_move} beats {player_move}")
        return player_points, computer_points + 1

    else:
        print("Remis")
        return player_points, computer_points


def gameplay():
    player_points = 0
    computer_points = 0

    while True:
        for move in MOVES:
            print(move, end='\t')
        print(f'\nWybierz jedną z powyższych figur lub wpisz "{USER_EXIT_COMMAND}" aby zakończyć: ')

        player_move = player_turn()
        computer_move = choice(MOVES)
        if player_move == USER_EXIT_COMMAND:
            break

        player_points, computer_points = compare_moves(player_move, computer_move, player_points, computer_points)

        print(f"Punkty gracza: {player_points}\nPunkty komputera: {computer_points}\n")


gameplay()
