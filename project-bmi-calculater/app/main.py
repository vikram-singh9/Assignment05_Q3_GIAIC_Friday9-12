import streamlit as st 


def bmi_calculater():
    weight = int(input("Enter your weight is kg: "))
    height = int(input("Enter your height is meters: "))





































































def main():
    print("Hello from app!")


if __name__ == "__main__":
    main()
    st.title("BMI Calculator")
    
    weight = st.number_input("Enter your weight (in kg)", min_value=0.0)
    height = st.number_input("Enter your height (in meters)", min_value=0.0)
    
    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = weight / (height ** 2)
            st.write(f"Your BMI is: {bmi:.2f}")
            
          
            if bmi < 18.5:
                st.warning("You are underweight")
                st.balloons()
            elif 18.5 <= bmi < 25:
                st.success("You have a normal weight")
                st.balloons()
            elif 25 <= bmi < 30:
                st.warning("You are overweight")
                
            else:
                st.error("You are obese")
        else:
            st.error("Please enter valid weight and height values")
