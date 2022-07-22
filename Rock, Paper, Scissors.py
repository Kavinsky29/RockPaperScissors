#This is a Rock, Paper or Scisors game made in Python using control statements and functions, just for fun

import random

def play():
    user = input("Please select 'r for Rock, 'p' for Paper, or 's' for Scisors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won the match!'

    return 'You lose :( '
    

def is_win(player, opponent):

    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True 

print(play())