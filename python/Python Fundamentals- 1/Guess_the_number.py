import random

n = 30

num = random.randint(1, n)

print("Guess the number, range: 1 to ", n)

count = 0 # No of attempts
while count <= n:
    guess = int(input("Guess and Enter a number: "))
    count += 1
    if guess == num:
        print("You guessed the correct number in "+ str(count)+ " attempts")
        break
    elif guess < num:
        print("You guessed a lower number")
    else:
        print("You guessed a higher number")

print("Game over!")

