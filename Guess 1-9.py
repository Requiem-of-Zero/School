import random

number = random.randint(1,9)
guess = int(input("Guess a number between 1-9: "))

times = 0

while guess != number :
        guess = int(input("Guess a number between 1-9: "))
        times += 1

if guess == number:
    print('Good guess')
    print('In:', str(times), "atempts", sep = ' ')