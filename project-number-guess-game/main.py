import random

computer = random.randint(1,10)
while True:
    user = int(input("enter your guess (1 to 10): "))
    if user == computer:
        print(f"Correct the number was {computer}")
        break
    else:
        print("try again...")
       