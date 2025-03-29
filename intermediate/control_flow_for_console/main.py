import random

def high_low_game(rounds=3):
    score = 0
    for _ in range(rounds):
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        print(f"Your number: {player_number}")
        guess = input("Is your number higher or lower than the computer's? (higher/lower): ").strip().lower()
        
        if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
            print("Correct! You get a point!")
            score += 1
        else:
            print("Wrong! No point this round.")
        
    print(f"Game over! Your final score: {score}/{rounds}")

high_low_game()
