def get_amount_price():
    amount_m_function = int(input('Enter the amount of money you have: '))
    price_a_function = int(input('What is the price of the apple you wish to purchase?: '))
    return amount_m_function, price_a_function

def maximum_apple():
    maximum_apple_function = int(amount_money/price_of_a)
    return maximum_apple_function

def amount_change():
    amount_change_function = int((amount_money)-(price_of_a*apple))
    return amount_change_function

def display_output(maximum_apple_function, amount_change_function):
    output_function = print(f"You can buy {apple} apples and your change is {change} pesos.")

amount_money, price_of_a = get_amount_price() #this ask the user's amount of money and the price of the apple he wants to buy
apple = maximum_apple() #this is the calculation of the maximum apple he can buy with the user's amount of money
change = amount_change() #this is the calculation of how much money the user's going to have after buying apples
display_output(apple, change) #this let the user know how many apple the user's can buy and how much money is left after buying