# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

rango = 100
n = 7
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, n, rango
    secret_number = random.randrange(0,rango)
    
    print "New Game. Range is from 0 to", rango
    print "Number of remaining guesses is", n


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global rango, n
    rango = 100
    n = int (math.ceil(math.log(100, 2)))
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global rango, n
    rango = 1000
    n = int (math.ceil(math.log(1000, 2)))
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global secret_number, n, rango
    guess = int(guess)
    n = n - 1
    ganar = False
    print "Guess was", guess
    print "Number of remaining guesses is", n
    if guess == secret_number:
        ganar = True
    elif guess < secret_number:
        opcion = "Higher"
    else:
        opcion = "Lower"
        
    if ganar == True:
        print "Correct!!!"
        print " "
        new_game()
    elif n == 0:
        print "You ran out of guesses. Number was", secret_number
        print " "
        new_game()
    else:
        print opcion
        
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)
# call new_game 
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
