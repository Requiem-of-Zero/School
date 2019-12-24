import random

comp_wins = 0
user_wins = 0

def choose_Option():
    user_choice = input('CHOOSE ROCK PAPER OR SCISSORS MOTHERFUCKER >')
    if user_choice in ["Rock", 'rock', 'r', 'R']:
        user_choice = 'r'
    elif user_choice in ["Paper", 'paper', 'p', 'P']:
        user_choice = 'p'
    elif user_choice in ['SCISSORS','Scissors', 'scissors', 's', 'S']:
        user_choice = 's'
    return user_choice
    
def computer_Option():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice = 'r'
    elif computer_choice == 2:
        computer_choice = 'p'
    else:
        computer_choice = 's'
    return computer_choice

while True:
    print('')

    user_choice = choose_Option()
    computer_choice = computer_Option()

    print('')

    if user_choice == 'r':
        if computer_choice == 'r':
            print('FUCK YOU GO AGAIN')
        elif computer_choice == 'p':
            print('HAHAH DUMBASS')
            comp_wins += 1
        elif computer_choice == 's':
            print('GOD DAMN IT FUCK YOU')
            user_wins += 1
    elif user_choice == 'p':
        if computer_choice == 'r':
            print('FUCK YOU')
            user_wins += 1
        elif computer_choice == 'p':
            print('FUCK YOU GO AGAIN')
        elif computer_choice == 's':
            print('HAHAHA IDIOTA')
            comp_wins += 1
    elif user_choice == 's':
        if computer_choice == 'r':
            print("HAHAHA YOU MORON")
            comp_wins += 1
        elif computer_choice == 'p':
            print("YOU GOT LUCKY AS FUCK")
            user_wins += 1
        elif computer_choice == 's':
            print('GOD DAMN IT GO AGAIN')

    print('')
    print('User Wins: ' + str(user_wins))
    print('Computer Wins: ' + str(comp_wins))
    print('')

    user_choice = input('PLAY AGAIN? (Y/N): ')
    if user_choice in ["Yes", "YES", "yes", "y", "Y"]:
        pass
    elif user_choice in ["NO", "No", "no", "n", "N"]:
        break
    else:
        break

        