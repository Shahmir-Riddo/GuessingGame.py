import random

#Set the text value

Text = 'Welcome to the Guessing Game'

print('\033[1;30;47m' + Text)

list1 = []
for x in range(5):
    list1.append(x)


print("Rules -")
print("You have to guess the right number to beat your opponent")

Guess = int(input("Guess a number from 0 - 5  : \n"))


Computer = random.choice(list1)
print("Your opponent guessed", Computer)

if Computer == Guess:
    print('\033[1;30;42m', "You Won!")

elif Computer > Guess or Computer < Guess:
    print('\033[1;30;41m', "You Lose")

else:
    print("Invalid Number!")