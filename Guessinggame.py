import random


Text = 'Welcome to the Guessing Game'

print('\033[1;30;47m' + Text)

list1 = []
for x in range(5):  
    list1.append(x)


print("Rules -")
print("You have to guess the right number to beat your opponent")
while True:

    Guess = int(input("Guess a number from 0 - 5  : \n"))

    Computer = random.choice(list1)
    print("Your opponent guessed", Computer)



    if Computer == Guess:
        print('\033[1;30;42m', "You Won!")

    elif Computer > Guess or Computer < Guess:
        print('\033[1;30;41m', "You Lose")

    else:
        print("Invalid Number")

    reminder = input("Do you want to play again? y/n :")
    if "n" in reminder:
        print("Game Finished")
        break

    else:
        continue


