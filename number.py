import random

secret_no=random.randint(1,100) #random number
tries_left = 7 #to track the number of attempts left in a loop or game. 

while tries_left > 0:
    try:
        guess=int(input("guess the number between 1 to 100(You have {tries_left} tries left):"))
        if guess == secret_no:
            print("congras your guess is correct.")
            break
        elif guess < secret_no:
            print("too low!")
        else:
            print("too high!")

        tries_left -=1
    except ValueError:
        print("invalid input.please entr a number")
if tries_left==0:
    print(f"you ran out of triess. the no was {secret_no}.")
