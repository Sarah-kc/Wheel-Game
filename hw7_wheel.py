# ----------------------------------------------------------
# --------          HW 7: wheel of fortune         ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Sarah Cryan
# Time spent on this problem: 3.5 hours
#
# Collaborators and sources: Help from Wael (Open Lab)
#   (List any collaborators or sources here.)
#
# ----------------------------------------------------------

# Complete the code below for wheel of fortune

import string
import random

# you can just _use_ this function in your code; you should not
# make any changes to it
def scoreboard(num_missed):
    ''' (int) -> 
    Print the scoreboard for the game
    '''
    print("---------------")
    scoreStr = "|"
    for i in range(1,8):
        if i <= num_missed:
            scoreStr += "X|"
        else:
            scoreStr += " |"
    print(scoreStr)
    print("---------------")

# your code should go between here and main
def get_guess():
    '''()->str
    Returns a single letter input in uppercase
    '''
# your code for this function should start here (you can remove
# the "pass" above)
    done = False
    while not done:
        guess = input('What is your guess? ')
        if guess not in string.ascii_letters or len(guess) != 1:
        #if either the guess isn't a letter or is greater than one character, the guess is not valid
            print("One letter, please!")

        else:
            done = True
        
    return guess.upper()


def update_game_state(secret_word, letter, guess_state):
    ''' (str, str, str) -> str
    Returns the newest version of the guess state, so if the guess
    is correct, it's correlating underscore will become the letter
    >>> update_game_state('LEAVES', 'V', '______')
    '___V__'
    >>> update_game_state('WINDY', 'W', '_IND_')
    'WIND_'
    >>> update_game_state('MUD', 'D', '_U_')
    '_UD'
    '''
    index = 0 
    for char in secret_word:
        if char == letter: #if any of the characters in the secret word match the guessed letter
            #the guess state will display the correct guesses
            guess_state=guess_state[:index]+letter+guess_state[index+1:]
        index+=1 #accumulates to keep track of the index for each character in the secret word
            
    return guess_state

def print_game_state(misses, previous_guesses, guess_state):
    '''(int, str, str) ->
    Prints the scoreboard for the user, including Xs to signify
    incorrect guesses, the current state of how many correct letters
    have been guessed, and which letters have been guessed
    >>> print_game_state(0, '', '___')
    ---------------
    | | | | | | | |
    ---------------
    _ _ _
    Already guessed: 
    >>> print_game_state(3, 'ZXF', '_U_')
    ---------------
    |X|X|X| | | | |
    ---------------
    _ U _
    Already guessed: ZXF
    >>> print_game_state(1, 'W', 'L_____')
    ---------------
    |X| | | | | | |
    ---------------
    L _ _ _ _ _
    Already guessed: W
    '''
    scoreboard(misses) #draws the scoreboard given how many misses have occured
    print(' '.join(list(guess_state))) #creates spaces between slots for the known and unknown letters of guess state
    print('Already guessed:', previous_guesses)

def one_game(secret):
    '''(str) ->
    Initiates and ends the game. It also checks
    if the guess has been entered before and tracks
    number of misses.
    '''
    guess_state = len(secret)*'_'
    previous_guesses = '' #keeps record of which guesses have been entered
    misses = 0 #keeps track of number of incorrect guesses
    while misses<7 and guess_state.strip()!=secret:
        print_game_state(misses, previous_guesses, guess_state)
        guessLetter = get_guess()
        if guessLetter in previous_guesses: #checks for duplicate answers
            print('You already guessed that')
        else:
            if guessLetter not in secret: #checks for incorrect answers & updates number of misses
                misses +=1
            else:
                guess_state = update_game_state(secret, guessLetter, guess_state)
                #if a correct letter is guessed, guess_state must be updated and show that a correct guess was made
            previous_guesses+=guessLetter
            #as long as the letter has been guessed before, all letter guesses will go into previous guesses
            
    if misses == 7: 
        print("Boo-hoo, you lost! The word was",secret)#output for if the player lost
    if guess_state.strip() == secret:
        print("Congratulations!")#output for if the player won

        
    

def main():
    '''() -> ()

    main function for playing hangperson
    '''
    words = ['SPRING', 'LEAVES', 'WARM', 'MUD', 'SUNNY', 'WINDY', 'RAINY']
    secret = random.choice(words)
    print("For testing, the secret word is", secret)
    one_game(secret)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()
