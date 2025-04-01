import streamlit as st
import random

st.title("Fun with Python! 🐍")
st.subheader("A collection of mini games and tools")

# Sidebar for navigation
activity = st.sidebar.selectbox(
    "Choose an activity",
    ["Number Guessing", "Coin Flip", "Dice Roll", "Random Quote"]
)

if activity == "Number Guessing":
    st.header("Number Guessing Game 🎲")
    st.write("I'm thinking of a number between 1 and 20...")
    
    number = random.randint(1, 20)
    guess = st.number_input("Enter your guess:", min_value=1, max_value=20)
    
    if st.button("Check!"):
        if guess == number:
            st.success("Congratulations! You got it right! 🎉")
            st.balloons()
        else:
            st.error(f"Sorry, the number was {number}. Try again!")

elif activity == "Coin Flip":
    st.header("Coin Flip 🪙")
    if st.button("Flip the coin!"):
        result = random.choice(["Heads", "Tails"])
        st.write(f"The coin shows: {result}")
        st.write("🪙" if result == "Heads" else "💫")

elif activity == "Dice Roll":
    st.header("Dice Roll 🎲")
    dice_sides = st.slider("How many sides?", 4, 20, 6)
    if st.button("Roll the dice!"):
        result = random.randint(1, dice_sides)
        st.write(f"You rolled a {result}!")
        if result == dice_sides:
            st.balloons()

else:
    st.header("Random Quote Generator 📜")
    quotes = [
        "Life is what happens while you're busy making other plans. - John Lennon",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "Code is like humor. When you have to explain it, it's bad. - Cory House",
        "Python is the second best language for everything. - Unknown"
    ]
    if st.button("Generate Quote"):
        st.write(random.choice(quotes))

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit and Python")
