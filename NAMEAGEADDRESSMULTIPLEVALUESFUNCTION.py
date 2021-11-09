def get_user_info():
    name_function = input("Enter your name: ")
    age_function = input("Enter your age: ")
    address_function = input("Enter your address: ")
    return name_function, age_function, address_function

def display_output(name_function, age_function, address_function):
    print(f"Hi, my name is {name}. I am {age} years old and I live in {address}.")

name, age, address = get_user_info() #this will get the name, age, and adress of the user
display_output(name, age, address) #this will display the info the user put in the program