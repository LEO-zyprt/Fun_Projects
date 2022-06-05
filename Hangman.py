from ast import If
from tkinter import E
from Hangmanword import words
import random
import string

def guess_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

#  the Usage of Set Every set element is unique (no duplicates) and must be immutable


def hangman():
    word = guess_valid_word(words)
    word_letters = set(word) # record the letter in the selected word
    used_letters = set() # record the letter that user has input
    alphabet = set(string.ascii_uppercase) # the total letters in English
    Lives = 6

    while len(word_letters)>0 and Lives > 0:
        # get user input
        user_letter = input('guess a letter:').upper()
        
        if user_letter in alphabet - used_letters: # first, you have gussed or not
            used_letters.add(user_letter)
            if user_letter in word_letters: # second, guess right or not
                word_letters.remove(user_letter) # next, we will use the length to know if the game is over
            
            else:
                Lives = Lives -1
        
        elif user_letter in used_letters:
            print('you have gussed the word, please try again:')
        
        else:
            print('please input a valid character:')

        print('you have input:',' '.join(used_letters)) #the way how join is used
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('you have',Lives,'lives left and your current word:',' '.join(word_list))

    if Lives == 0:
        print('sorry, you have died')
    else:
        print('you have guessed right')

print(hangman())







