"""
#########################################################################
# Rock Paper Scissors game using Python and random()                    #
# Copyright (C) 2022 Avino Domenico                                     #
#                                                                       #
# This program is free software: you can redistribute it and/or modify  #
#########################################################################
"""

import random
import os

player_score = 0
computer_score = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    global player_score
    global computer_score
    player_choice = ''
    computer_choice = ''
    while True:
        while True:
            player_choice = input("\nEnter your choice: ").lower()
            if player_choice == 'rock' or player_choice == 'paper' or player_choice == 'scissors':
                break
            else:
                print("\nInvalid choice. Please try again.")
        while True:
            computer_choice = random.choice(['rock', 'paper', 'scissors'])
            if computer_choice == 'rock' or computer_choice == 'paper' or computer_choice == 'scissors':
                break
        if player_choice == computer_choice:
            print("\nTie!")
        elif player_choice == 'rock':
            if computer_choice == 'paper':
                print("\nComputer wins!")
                computer_score += 1
            else:
                print("\nPlayer wins!")
                player_score += 1
        elif player_choice == 'paper':
            if computer_choice == 'scissors':
                print("\nComputer wins!")
                computer_score += 1
            else:
                print("\nPlayer wins!")
                player_score += 1
        elif player_choice == 'scissors':
            if computer_choice == 'rock':
                print("\nComputer wins!")
                computer_score += 1
            else:
                print("\nPlayer wins!")
                player_score += 1
        if player_score == 3:
            print("\nPlayer wins the game!")
            break
        elif computer_score == 3:
            print("\nComputer wins the game!")
            break

while True:
    clear_screen()
    print("\nRock Paper Scissors")
    print("\nPlayer: {}".format(player_score))
    print("Computer: {}".format(computer_score))

    if player_score == 3 or computer_score == 3:
        break
    main()