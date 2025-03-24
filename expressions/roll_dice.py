import random

def roll_dice():
    dice_rolls = 6

    die1 = random.randint(1,dice_rolls)
    die2 = random.randint(1,dice_rolls)

    sum = die1 + die2

    print(f"The sum of die {die1} and die {die2} is {sum}.")

if __name__ == "__main__":
    roll_dice()