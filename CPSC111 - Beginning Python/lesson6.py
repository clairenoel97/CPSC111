#advanced if statements

'''
Example Problem
    write a game to have the user guess a number
'''

def guess_number():
    num_to_guess = 4
    players_guess = int(input("Please enter a number between 1 and 10 inclusive"))

    if players_guess == num_to_guess:
        print("Congrats! You got it!")
    else:
        print("Unfortunately, you guessed the number incorrectly; however, I will give you a hint!")

    if players_guess > num_to_guess:
        print("Your guess was too high")

    if players_guess < num_to_guess:
        print("Your guess was too low")


'''
Nested if statements
'''

num_guesses = 3

print("Please enter a number between 1 and 10 inclusive")
players_guess = int(input())

if players_guess != num_to_guess:
    if num_guesses > 0:
        print("You are wrong but you get to try again")

# the above nested if can collapse into a compound condition
if players_guess != num_to_guess and num_guesses > 0:
    print("You are wrong but you get to try again")


'''
Multiple-Alternative if statements
'''

num_to_guess = 4
players_guess = 0

print("Please enter a number between 1 and 10 inclusive")
players_guess = int(input())

# a guess is either equal to, greater than, or less than
if players_guess == num_to_guess: # BC 1
    print("Congrats, you guessed the number correctly")
elif players_guess > num_to_guess: # BC 2
    print("Your guess was too high")
else: # players_guess < num_to_guess
    print("Your guess was too low")
