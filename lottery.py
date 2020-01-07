import random

def get_Tickets():
    for ticket in range(5):
        tickets = random.randint(1,53)
        print(tickets)

print("")
print("Hello, would you like some lottery numbers?")
print("")

user_input = input("Yes/No: ")

if user_input in ["Yes", "YES", "yes", "y", "Y"]:
    print("")
    get_Tickets()
    print("")
elif user_input in ["No", "no", "NO", "n", "N"]:
    print("")
    print("Ok fine")
else:
    print("You straight weird that wasn't even a selection")
