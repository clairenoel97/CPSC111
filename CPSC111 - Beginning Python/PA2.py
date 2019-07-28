#assigment 2

'''
Write a program that simulates a night out on the town! The night out on the town is going to include the following activities:
    1. dinner
    2. concert

    The program will keep track of the amount of money spent for each activity (and associated car parking for the activity), including tax and tip where appropriate

    Program Details:
        1. state sales tax (percent)
        2. price to park for dinner
        3. price of meal before tax
        4. dinner tip (percent)
        5. price to park for the concert
        6. price of the concert before tax

    the output:
        1. total money spent for each activity (dinner tab and concert)
        2. total money spent parking the user's car for the activities (dinner parking + concert parking)
        3. total money spent for the night out

'''
import math
import pip
import matplotlib.pyplot as plt

def display_instructions():
    '''
    prints the instructions describing the use of the program to the user
    '''

    print("Welcome to the night out simulator! This program will prompt you for the sales tax (as a percent) in your state. \nThen it will walk you through your night out on the town, starting with dinner and ending with a concert! \nThe total amount of money spent for the evening will be kept track of, so you know how much your credit card bill will be!\n\n")

def get_tax_percent():
    '''
    prompts the user for the state sales tax as a percent and returns the sales tax percent
    '''

    sales_tax = float(input("What is the sales tax in your state (as a percentage)? "))
    return (sales_tax / 100)

def get_tip_percent():
    '''
    prompts the user for what percentage of the bill (meal price + tax) they would like to tip and returns the tip percent
    '''

    dinner_tip = float(input("What percentage do you want to leave as a tip? "))
    return dinner_tip / 100

def get_price(activity_label):
    '''
    prompts the user to enter the price for activity_label and returns a string prepresenting the city
    '''
    if activity_label == "parking":
        return "How much does %s cost? " %(activity_label)
    else:
        return ("How much does %s cost before tax? " %(activity_label))

def calculate_tax(price, tax_percent):
    '''
    price: float representing the cost of the activity
    tax_percent: float representing the sales tax percent
    computes the tax for price and returns the result as a float
    '''
    tax_amount = price * (tax_percent)
    return float(tax_amount)

def calculate_tip(price, tip_percent):
    '''
    price: floar representing the cost of the activity
    tip_percent: float representing the percentage the user would like to tip
    computers the tip for price and returns the result as a float
    '''
    tip_amount = price * (tip_percent)
    return float(tip_amount)

def round_up_to_nearest_dollar(price):
    '''
    price: float representing the cost of the activity
    rounds price to the nearest dollar and returns the result as a floating point number
    '''

    rounded_price = math.ceil(price)
    return float(rounded_price)

def park_car():
    '''
    prompts the user for the cost to park their car and returns the  result as a float
    calls get_price()
    '''

    parking_price = float(input(get_price("parking")))
    return parking_price

def go_to_dinner(tax_percent):
    '''
    tax_percent: float representing the sales tax percent
    computes the total cost of dinner and returns the result as a float
    '''
    dinner_price = float(input(get_price("dinner")))
    tip_percent = get_tip_percent()
    tax_amount = calculate_tax(dinner_price, tax_percent)
    tip_amount = calculate_tip(dinner_price, tip_percent)
    total_dinner = dinner_price + tax_amount + tip_amount
    rounded_amount = round_up_to_nearest_dollar(total_dinner)
    return float(rounded_amount)

def go_to_concert(tax_percent):
    '''
    tax_percent: a float representing the sales tax percent
    computes the total cost of the concert and returns the result as a float
    '''
    concert_price = float(input(get_price("concert")))
    tax_amount = calculate_tax(concert_price, tax_percent)
    concert_total = concert_price + tax_amount

    return float(concert_total)

def display_money_spent(dinner_spent, concert_spent, parking_spent):
    '''
    dinner_spent: money spent on dinner
    concert_spent: money spent on concert
    parking_spent: money spent on parking
    '''

    dinner = print("After tax and tip, you spent $%.2f on dinner." %(dinner_spent))
    concert = print("After tax, you spent $%.2f on the concert." %(concert_spent))
    parking = print("In total, you spent $%.2f on parking." %(parking_spent))

    total = dinner_spent + concert_spent + parking_spent
    print("That means, you spent $%.2f this evening. Sounds like a lot of fun!" %(total))

def plot_money_spent(label1, price1, label2, price2, label3, price3):
    '''
    111 STUDENTS: THIS IS THE FUNCTION YOU WILL CALL FOR THE **BONUS** TASK
    Accepts 3 pairs of strings (activity labels) and 3 floats (money spent)
    Ordering of the parameters is 3 pairs of activity label string, money spent value

    Uses matplotlib functions to plot a bar graph of the activity prices.
    Save the plot by clicking on the save button on the toolbar of the plot window.
    Press the X to close the window when you are done.

    This function does not return anything.
    '''
    x = [0, 1, 2]
    x_labels = [label1, label2, label3]
    y = [price1, price2, price3]
    plt.bar(x, y)
    plt.xticks(x, x_labels, ha='left')
    plt.xlabel("Activity")
    plt.ylabel("Price in Dollars")
    plt.tight_layout()
    # show the window
    plt.show()

def main():
    display_instructions()
    tax_percent = get_tax_percent()
    dinner_parking = park_car()
    dinner_amount = go_to_dinner(tax_percent)
    concert_parking = park_car()
    concert_amount = go_to_concert(tax_percent)
    parking_amount = dinner_parking + concert_parking
    print()
    display_money_spent(dinner_amount, concert_amount, parking_amount)
    plot_money_spent("Dinner", dinner_amount, "Concert", concert_amount, "Parking", parking_amount)

main()
