
"""import random
# generate a random number between 1 to 100
secret_number = random.randint(1,100)

print("welcome to the number gussing game !")
print("i am thinking number between 1 to 100")

attempt = 0

while True:
    guess = int(input("Enter Your Guess: "))
    attempt += 1

    if guess < secret_number:
        print("Too low! Try Again. ")
    elif guess > secret_number:
        print("Too High! Try AGAIN. ")
    else:
        print(f"congrates! you guessed the number in {attempt} attempts")
        break"""

import random
# guessing a random number between 1 to 100
secret_number = random.randint(1, 100)

print("welcome to the number guessing game ")
print("i am thinking a number between 1 to 100 ")

attempt = 0

while True: 
    guess = int(input("Enter Your Guess Try Again  "))
    attempt += 1

    if guess < secret_number:
        print("too low try again ")
    elif guess > secret_number:
        print("too high try again")
    else:
        print(f"congrates you guessed the number in {attempt} attempt ")
        break