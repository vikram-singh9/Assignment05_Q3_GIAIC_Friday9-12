import streamlit as st
import random 
import string

def password_generator (length, use_digits, use_special):
    charactors = string.ascii_letters # a to z and A TO Z
    if use_digits:
        charactors += string.digits

    if use_special:
        charactors += string.punctuation
    
    return "".join(random.choice(charactors) for _ in range(length))


st.title("🤠Password Generator Poject👀")
length = st.slider("Select passwprd range", min_value=5, max_value=30, value=8)
use_digit = st.checkbox("Add digits")
use_special = st.checkbox("Add Special Charactors")

if st.button(f"Generate Password"):
    password = password_generator(length, use_digit, use_special)
    st.write(password)