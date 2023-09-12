import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter a number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Choose a number between 2 and 4: ")
    else:
        print("Invalid, Try again!")

max_score = 50
player_scores = [0 for i in range(players)]

# while max(player_scores) < max_score:
