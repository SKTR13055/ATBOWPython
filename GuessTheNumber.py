#THIS IS GUESS THE NUMBER GAME
import random
secretnumber = random.randint(1,100)
print("I am thinking of a number can you guess what the number is?")

#ASKS THE PLAYER TO GUESS THE NUMBER 6 TIMES
for guessesTaken in range(1,7):
    print('guess the number')
    guess = int(input())
    
    if(guess < secretnumber):
        print("The number is too low")
    elif(guess > secretnumber):
        print("The number is too high")
    else:
        break #THIS CONDITION IS THE CORRECT GUESS!
    
if guess == secretnumber:
    print("Amazing! You've guess the number in " +str(guessesTaken) + " guesses!")
else:
    print('Nah the number I was thinking of was the number ' +str(secretnumber))    