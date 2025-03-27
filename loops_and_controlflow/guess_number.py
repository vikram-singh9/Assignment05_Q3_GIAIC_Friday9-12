import random

secret_number = random.randint(1, 100)
print("Think a number bewteen 1 and 100")
def main():
    user_guess = int(input("Enter your guess: "))
    while True:
        if user_guess > secret_number:
            print("HINT: Your guess is too high")
            break
        if user_guess < secret_number:
            print("HINT: Your guess is too low")
            break
        if user_guess == secret_number:
            print("You guessed the correct number")
            break


if __name__ == '__main__':
    main()