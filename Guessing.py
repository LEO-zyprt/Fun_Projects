import random

def guess(x):
    random_num = random.randint(1,x)
    guess_number = 0
    while guess_number != random_num:
        guess_number = int(input(f'please input the number from 1 to {x}:')) # keep it in the loop as it will show many times
        if guess_number > random_num:
            print("your input is too big")
        elif guess_number < random_num:
            print("your input is too small")
    print("yay, congrats, you are guessing right")

# guess(20)


def computer_guess(x):
    low = 1
    high = x
    feedback = " "

    while feedback != "c":
        if low != high: 
            guess_number = random.randint(low, high) # remember that low and high are dynamic
        else:
            guess_number = high
        feedback = input(f"choose from three if the number {guess_number} is Low(L), \
            or high(H), or correct(C): ").lower()
        if feedback == "h":
            high = guess_number-1
        elif feedback == "l":
            low = guess_number+1

    print('yay, congrats, the computer guessed correctly!')

computer_guess(100)