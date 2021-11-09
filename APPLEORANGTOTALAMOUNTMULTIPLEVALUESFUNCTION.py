def display_price_fruits():
    print("The price of the apple is 20 pesos while the price of the orange is 25 pesos.")

def apple_and_orange():
    price_a_function = 20
    pieces_a_function = int(input('How many apples do you want to buy?: '))
    price_o_function = 25
    pieces_o_function = int(input('How many oranges do you want to buy?: '))
    return price_a_function, pieces_a_function, price_o_function, pieces_o_function

def total_amount(price_a_function, pieces_a_function, price_o_function, pieces_o_function):
    total_amount_function = int((price_of_a*pieces_of_a) + (price_of_o*pieces_of_o))
    return total_amount_function

def display_amount(total_amount_function):
    print(f"The total amount is {amount}.")

display_price_fruits() #this let the user know the prices of apple and orange.
price_of_a, pieces_of_a, price_of_o, pieces_of_o = apple_and_orange() #this programs the prices of the apple and orange. it also ask the user how many apple and oranges he/she wants to buy.
amount = total_amount(price_of_a, pieces_of_a ,price_of_o, pieces_of_o) #this is the calculation of the user's total amount of buying apples and oranges.
display_amount(amount) #this let the user know the total amount the user need to pay.