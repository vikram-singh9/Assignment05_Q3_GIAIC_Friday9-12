import streamlit as st
import random

st.title("Rock Paper Scissors Game 🎮")
st.subheader("Play against the computer! 🤖")

choices = ["rock", "paper", "scissors"]


player = st.radio("Choose your move:", choices)

if st.button("Play!"):
    computer = random.choice(choices)
    
    
    st.write(f"You chose: {player}")
    st.write(f"Computer chose: {computer}")
    
    
    if player == computer:
        st.info("It's a tie! 🤝")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        st.success("You win! 🎉")
        st.balloons()
    else:
        st.error("Computer wins! 😔")

