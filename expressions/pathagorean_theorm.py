import math 


ab = float(input("Enter the length of AB=> "))
ac = float(input("Enter the length of AC=> "))


bc = math.sqrt(ab**2 + ac**2)

print(f"The length of BC (the hypotenuse) is: {bc}")