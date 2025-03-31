import streamlit as st 


def main():
    print("Hello from app!")


if __name__ == "__main__":
    main()
    st.title("BMI Calculator")
    st.write("Enter your height and weight to calculate your BMI")

    # Get user inputs
    weight = st.number_input("Enter your weight (in kg)", min_value=1.0, max_value=500.0, value=70.0)
    height = st.number_input("Enter your height (in meters)", min_value=0.1, max_value=3.0, value=1.7)

    # Calculate BMI when button is pressed
    if st.button("Calculate BMI"):
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")
        
        # Display BMI category
        if bmi < 18.5:
            st.warning("You are underweight")
        elif bmi < 25:
            st.success("You have a normal weight")
        elif bmi < 30:
            st.warning("You are overweight") 
        else:
            st.error("You are obese")
            
        # Display BMI chart
        st.write("\nBMI Categories:")
        st.write("Underweight = <18.5")
        st.write("Normal weight = 18.5–24.9") 
        st.write("Overweight = 25–29.9")
        st.write("Obesity = BMI of 30 or greater")
