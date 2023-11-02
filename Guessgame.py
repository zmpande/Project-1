#Challenge 1
#Guess game

import random

#choosing the number randomly between 1 and 10
num = random.randint(1,10)
#database where the numbers are stored
guess = ""
# guess is integer

while guess != num:
    #test the error
    try:
        guess = int(input("guess a number between 1 and 10: "))

    #handle the error
    except:
        print("You have entered an invalid input, please try again")
    else:
        if guess == num:
            print("congratulations! you won!")
            break
        elif (guess<1 or guess>10):
            print("The number is outside the range, Please enter the number between 1 and 10")
        elif guess > num:
            print("The number is too high. Try again!")
        elif guess < num:
            print("The number is too low. Try again!")


