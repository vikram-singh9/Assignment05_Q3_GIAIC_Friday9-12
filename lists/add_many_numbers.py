def sum_of_numbers(numbers):
    total = 0  
    for num in numbers: 
        total = total + num  # Har number ko total mein add karte jayenge
    return total 

my_list = [1, 2, 3, 4]
result = sum_of_numbers(my_list)
print(f"Sum of {my_list} is: {result}")