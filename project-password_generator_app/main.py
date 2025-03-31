import random 
import string

def password_generator(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# Example usage
if __name__ == "__main__":
    print(password_generator(10))


