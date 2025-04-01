import streamlit as st 

st.title("BMI calculater 📱") 
st.subheader("Calculate your BMI in now very easy 😍")

weight = st.number_input("Enter your weight in kg: ", value=0)
height = st.number_input("Enter your height in meters: ", value=0)

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        st.write(f"your bmi is: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("You are underweight!")
        elif 18.5 <= bmi < 25:
            st.success("You are normal weight!")
            st.balloons()
        elif 25 <= bmi < 30:
            st.info("You are overweight!")
        else:
            st.error("You are Obese!!!")
    else:
        st.write("Please enter the valid input!")
    




































































