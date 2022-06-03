import random
number = random.randint(0,100)
chances = 0


print("Number Guessing Name")
print("Guess a number between 1 - 100")



while chances < 7 :
    
    guess = int(input("Enter Your Guess: "))

    chances=chances+1
    if guess < number:
        print("Guess was high: Guess a number higher than ",guess)
    elif guess > number:
        print("Guess was low: Guess a number lower than ",guess)
    elif guess == number:
        print("Congratulations!!")

if chances == 7 and guess!=number:
    print("You Lose!!")
    print("The number is ",number)

