# Function jo list mein teen copies add karega
def add_three_copies(my_list, item):
    my_list.append(item)  # Pehli copy
    my_list.append(item)  # Dusri copy
    my_list.append(item)  # Teesri copy

# Main program
print("Enter a message to copy: ", end="")
message = input()

# Khali list banayi
items = []

# List ko pehle dikhana
print("List before:", items)

# Function call kiya, kuch return nahi kiya
add_three_copies(items, message)

# List ko baad mein dikhana
print("List after:", items)