def mars_weight():
    earth_weight = float(input("Enter your weight on Earth (kg): "))
    mars_weight = round(earth_weight * 0.378, 2)
    print(f"Your weight on Mars would be: {mars_weight} kg")

mars_weight()
