noun = input("Enter the noun")

# Print the completed story
print("\nHere's your Mad Libs story:")
print(story)

# Ask if they want to play again
play_again = input("\nWould you like to play again? (yes/no): ")
if play_again.lower() == "yes":
    print("\nLet's play again!\n")
    # The game would restart here
else:
    print("\nThanks for playing Mad Libs! Goodbye!")
