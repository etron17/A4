# Student name: Dojae Kim
# Student number: 400420323
# Student email: kim408@mcmaster.ca
# Lecture: SFWRTECH 3PR3
# Assignment1

"""
Rock Paper Scissors Spock Lizard game. The program will have two players and each of them produce a random outcome,
i.e., Rock, paper, scissor, spock, or lizard. Based on each player’s outcome, determine the winner.
The rules of the game are:
    Spock beats scissors and rock, but loses to paper and lizard.
    Lizard beats Spock and paper, but loses to rock and scissors.
    Rock beats scissors and lizard, but loses to paper and Spock.
    Paper beats rock and Spock, but loses to scissors and lizard.
    Scissors beats paper and lizard, but loses to rock and Spock.
"""

import random

hand_shapes = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Spock", 5: "Lizard"}

# The hand shapes will be randomly generated
player_1 = random.randint(1, 5)
player_2 = random.randint(1, 5)

# If both players choose the same hand shape, the game is tied
if player_1 == player_2:
    print(f'Player 1 chose "{hand_shapes[player_1]}" ---- Player 2 chose "{hand_shapes[player_2]}" -> The game is tied!')

elif (player_1 == 1 and player_2 == 3) or (player_1 == 1 and player_2 == 5):
    print(f'Player 1 chose "{hand_shapes[player_1]}" ---- Player 2 chose "{hand_shapes[player_2]}" -> Player 1 win!')

elif (player_1 == 3 and player_2 == 1) or (player_1 == 5 and player_2 == 1):
    print(f'Player 1 chose "{hand_shapes[player_1]}" ---- Player 2 chose "{hand_shapes[player_2]}" -> Player 2 win!')

elif (player_1 == 2 and player_2 == 1) or (player_1 == 2 and player_2 == 4):
    print(f'Player 1 chose "{hand_shapes[player_1]}" ---- Player 2 chose "{hand_shapes[player_2]}" -> Player 1 win!')

elif (player_1 == 1 and player_2 == 2) or (player_1 == 4 and player_2 == 2):
    print(f'Player 1 chose "{hand_shapes[player_1]}" ---- Player 2 chose "{hand_shapes[player_2]}" -> Player 2 win!')

elif (player_1 == 3 and player_2 == 2) or (player_1 == 3 and player_2 == 5):
    print(f'Player 1 chose "{hand_shapes[player_1]}" ---- Player 2 chose "{hand_shapes[player_2]}" -> Player 1 win!')

elif (player_1 == 2 and player_2 == 3) or (player_1 == 5 and player_2 == 3):
    print(f'Player 1 chose "{hand_shapes[player_1]}" ---- Player 2 chose "{hand_shapes[player_2]}" -> Player 2 win!')

elif (player_1 == 4 and player_2 == 3) or (player_1 == 4 and player_2 == 1):
    print(f'Player 1 chose "{hand_shapes[player_1]}" ---- Player 2 chose "{hand_shapes[player_2]}" -> Player 1 win!')

elif (player_1 == 3 and player_2 == 4) or (player_1 == 1 and player_2 == 4):
    print(f'Player 1 chose "{hand_shapes[player_1]}" ---- Player 2 chose "{hand_shapes[player_2]}" -> Player 2 win!')

elif (player_1 == 5 and player_2 == 4) or (player_1 == 5 and player_2 == 2):
    print(f'Player 1 chose "{hand_shapes[player_1]}" ---- Player 2 chose "{hand_shapes[player_2]}" -> Player 1 win!')

elif (player_1 == 4 and player_2 == 5) or (player_1 == 2 and player_2 == 5):
    print(f'Player 1 chose "{hand_shapes[player_1]}" ---- Player 2 chose "{hand_shapes[player_2]}" -> Player 2 win!')



