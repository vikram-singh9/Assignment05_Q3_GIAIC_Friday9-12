noun = input("Enter the noun")
verb = input("Enter the verb")
adjective = input("Enter the adjective")

story = print(f"""
A Crazy Adventure

One day, a {adjective} {noun} decided to {verb} in the {adjective} park.
Suddenly, a {adjective} animal appeared and started to {verb}.
The {noun} was so {adjective} that it {verb} into a {adjective} place.

After that, a {adjective} vikram arrived and said, "aaaen!"
Everyone {verb} and had a {adjective} day!
""")


print("\nHere's your Mad Libs story:")
print(story)

play_again = input("Do you like to play again: (yes/no)")
if play_again.lower() == "yes":
    print("let's play again!")
else:
    print("don't forget to come back")