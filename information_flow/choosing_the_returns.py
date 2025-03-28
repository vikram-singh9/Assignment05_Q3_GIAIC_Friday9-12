ADULT_AGE = 19
def is_adult(age):
    return age >= ADULT_AGE

age = int(input("How old is this person?: "))
print(is_adult(age))