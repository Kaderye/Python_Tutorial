# NUMBER GUESSING GAME
# Make a variable, like winning _number and assign any number to it
# Ask user to guess a number
# if user guessed correctly then print "You win"
# if user didn't guessed correctly then:
# if user gussed lower than actual number then print "Too Low"
# if user guessed higher than actual number then prnt "Too High"

# google, how to generate random number in python to generate random winning number

# take a random nummber as winning number
import random
winning_number = random.randint(0,9)
#print(f"The winning number is {winning_number}")

# user input a number as guess number
guesse_number = int(input("Enter a guesse number: "))
print(f"The guesse number is {guesse_number}")

# condition
if (guesse_number == winning_number):
    print("You win")
else:
    if (guesse_number < winning_number):
        print(f"guesse number {guesse_number} is lower than winning number {winning_number}")
        print("Too low")
    else:
        print(f"guesse number {guesse_number} is higher than winning number {winning_number}")
        print("Too High")

