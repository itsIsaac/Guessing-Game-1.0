import random
import sys

enter = ("Please Press Enter To Continue...")

print ("Hello! Welcome to a Guessing game!")
print ("Please Guess A number between 1 - 3")
computernum = random.randint (1,3)
Guess1 = input ("My First Guess Is: ")
if Guess1 == computernum:
    print ("You Win!")
    input (enter)
    ("SystemExit")
else:
    print ("Sorry, try again!")
    print ("You Have 2 Guesses Remaining!")
    Guess2 = input ("My Second Guess Is: ")
if Guess2 == computernum:
    print ("Wow, Congrats you Win!")
    input (enter)
    ("SystemExit")
else:
    print ("Final Guess!")
    Guess3 = input ("My Final Guess Is: ")
if  Guess3 == computernum:
    print ("Congrats you win!")
    ("SystemExit")
else:
    print ("Sorry, you lose the game!")
computernum = input (computernum)
print( "The computers number was "+computernum)
input (enter)
("SystemExit")
    
