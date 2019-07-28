#Assignment 1
'''
We will be making a chatbot

1. find out the name of the user (string)
2. find out where the user is from (string)
3. find out when the user was born (int)
4. find out the users dream car (string)
5. find out how much the dream car costs (floats)
    A comment about how expensive the car is, such as "Gee, that is spendy."
    Find out how many years the user would take a loan out to pay for <car> (integer)
    Find out what annual interest rate (percent) the user expects to get for <car> (float)
    Reply with the expected monthly payment and total amount of money the user would pay
    for <car> (car price + interest), such as "Your monthly payment for the <car>
    is <monthly payment>, that is a total of <total cal cost>!.
6. Say goodbye to <user's name>
'''

def chatbot():
    name = str(input("Hello there! My name is CarBot. What is your name?\n"))
    state = str(input("Hello " + name + ", it is great to meet you!\n" +
    name + ", where are you from?\n"))
    year = int(input(state + " sounds like a pleasant place to grow up. Hmmmm what else can I ask you" +
    "... oh! What year were you born?\n"))
    current_year = 2019
    age = current_year - year
    carbot_age = 5
    age_compared = age / carbot_age
    car = str(input("You are " + str(age) + " years old, that makes you " + str(age_compared) + " times as old as I am!" +
    " I'm only " + str(carbot_age) + " years YOUNG!\n" + "What is your dream car?\n"))
    price = float(input("Wow, I have always wanted a " + car + " as well. How much does a " + car + " cost?\n"))
    interest = float(input("Gee, that is spendy! What is a reasonable yearly interest rate on a beautiful car like that?\n"))
    year_loan = int(input("And if you had to take out a loan to buy the " + car + ", how many years would you take the loan out for?\n"))
    monthly_interest_rate = (interest / 100) / 12
    monthly_payment = (monthly_interest_rate * price) / (1 - ((1 + monthly_interest_rate) ** -(year_loan * 12)))
    total_price = monthly_payment * 12 * year_loan
    print("If you bought the " + car + ", you would have a monthly payment of $%.2f, hopefully that is a reasonable for your budget. That's a total of $%.2f! I hope you can make the purchase!\nAnyways, I gotta go. It's been nice chattin' with ya %s :)" %(monthly_payment, total_price, name))

    mpg = float(input("Actually, before I go, can I ask you what the MPG of a %s is?\n" %(car)))
    if mpg > 34.1:
        print("Wow! The %s has more than 34.1 MPG, nice!")
    else:
        print("I guess the US government won't include your car in the new fleet of vehicles...")

chatbot()
