import random

print("Hello there, what is your name? ")
name = input()

def main():
    try:
        times = 0

        number = random.randint(1,15)
        guess = int(input(name + " guess a number between 1 and 15: "))

        while guess != number:
            if guess < number:
                print(name + " you need to guess higher. Try again.")
                guess = int(input("\nGuess a number between 1 and 15: "))
            else:
                print(name + " you need to guess lower. Try again.")
                guess = int(input("\nGuess a number between 1 and 15: "))
            times += 1
        if guess == number:
            print("Congrats " + name + ",you got it right in:", times,'attempts', sep=' ')
        restart = input("Would you like to restart game? Enter 'Yes': ")
        if(restart == 'Yes'):
            main()
        else:
            print('ok fk you too')
    except:
        print("Sorry I don't understand")
        main()
        guess = int(input("Guess a NUMBER between 1 and 15: "))
    
main()
