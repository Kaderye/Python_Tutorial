
# take a random number
import random
winning_number = random.randint(1,100)
# print(winning_number)
guesse = 1
# guesse a number
guesse_number = int(input("Enter a guesse number: "))

game_over = False

while not game_over:
    if (guesse_number == winning_number):
        print(f"You win, success in {guesse} times")
        game_over = True
    else:
        if (guesse_number < winning_number):
            print(f"guesse number {guesse_number} is lower than winning number")
            print("Too low")
        else:
            print(f"guesse number {guesse_number} is higher than winning number")
            print("Too High")
        guesse += 1
        guesse_number = int(input("Again guesse number: "))

            # DRY : Don't Repeat Yourself



