from random import randint

moves = ["Paper", "Rock", "Scissors", "Spock", "Lizard", "Stop"]

beats = {
    "Paper": ["Rock", "Spock"],
    "Rock": ["Scissors", "Lizard"],
    "Scissors": ["Paper", "Lizard"],
    "Spock": ["Rock", "Scissors"],
    "Lizard": ["Paper", "Spock"]
}


def player_turn():
    player_move = input()
    player_move = player_move.title()

    while player_move not in moves and player_move != "Stop":
        print("Zły ruch, spróbuj ponownie: ")
        player_move = input()
        player_move = player_move.title()

    return player_move


def gameplay():
    print('Paper\nRock\nScissors\nSpock\nLizard\nWybierz jedną z powyższych figur lub wpisz "Stop" aby zakończyć'
          ' program: ')
    player_points = 0
    computer_points = 0
    game_on = True
    while game_on:
        player_move = player_turn()
        computer_move = moves[randint(0, 4)]
        if player_move == "Stop":
            game_on = False

        if game_on:
            if computer_move in beats[player_move]:
                player_points += 1
            elif player_move in beats[computer_move]:
                computer_points += 1
            else:
                print("Remis")

        print(f"Punkty gracza: {player_points}\nPunkty komputera: {computer_points}")


gameplay()
