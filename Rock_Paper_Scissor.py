import random

def play():
    your_choice = input("please show your choice:'r' for rock, 's' for scissor, 'p' for paper:\n")#注意\n放在引号内
    computer_choice = random.choice(['r','s','p'])
    if (your_choice != 'r') and (your_choice != 's') and (your_choice != 'p'):
        return 'please run again' #please use return instead of print

    else:
        if your_choice == computer_choice:
            return 'it\'s a tie'
        elif is_win(your_choice, computer_choice):
            return 'You Win!'
        #there is no need to add an elif here as the only left choice is you lose
        return 'You lose!'


def is_win(winner, loser):
    if (winner=='s'and loser=='p') or (winner=='p'and loser=='r') or (winner=='r'and loser=='s'): 
        #if i use &, its not work, "and" is fine here
        return True #return ture is behind if, there is no need to return at the left
    

print(play())