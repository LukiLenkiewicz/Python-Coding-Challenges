from random import randint

computer_moves = {
    1: "Paper",
    2: "Rock",
    3: "Scissors",
    4: "Spock",
    5: "Lizard"
}

beats = {
    "Paper": ["Rock", "Spock"],
    "Rock": ["Scissors", "Lizard"],
    "Scissors": ["Paper", "Lizard"],
    "Spock": ["Rock", "Scissors"],
    "Lizard": ["Paper", "Spock"]
}


def gameplay():
    player_points = 0
    computer_points = 0
    game_on = True
    while game_on:
        player_move = input("Paper\nRock\nScissors\nSpock\nLizard\nWybierz jedną z powyższych figur: ")
        computer_move = computer_moves[randint(1, 5)]
        if player_move == "STOP": game_on = False
        if game_on:
            """Do tych ifów dorobić funkcje"""
            if computer_move in beats[player_move]:
                player_points += 1
            elif player_move in beats[computer_move]:
                computer_points += 1
            else:
                print("Remis")

        print(f"Punkty gracza: {player_points}\nPunkty komputera: {computer_points}")

gameplay()
