#advanced loops

'''
break statements
    sometimes we need to 'break' out of a loop early, i.e. before the boolean conditions is 'false'. We can accomplish this anywhere in the body of the loop with the break statement

    ex:
'''

while True:
    word = input("Please enter a word: ")
    if word == "stop":
        break

'''
nested loops
    loops within loops
    be cautious of:
        indenting the bodies of the loops correctly
        progress toward all of the boolean conditions eventually being false
'''

# ### Example Problem #1
# Write a program to prompt the user to enter the number of lines of stars to print. On each line, there will be as many stars printed as the line number. For example, if the user enters 5, the first line will have 1 star, the second line will have 2 stars, etc., until the 5th line, which will have 5 stars:
#
# ```
# *
# **
# ***
# ****
# *****
# ```

# In[10]:

num_lines = int(input("Number of lines: "))
for i in range(num_lines):
    for j in range(0, i + 1):
        print("*", end="")
    print()


# ### Example Problem #2
# Now try and print it the other way, with `num_lines` stars on the first line, `num_lines - 1` on the second, etc.

# In[1]:

num_lines = int(input("Number of lines: "))
for i in range(num_lines):
    for j in range(i, num_lines):
        print("*", end="")
    print()


# ### Example Problem #2 Alternative Solution
# We could rewrite the above nested loop to instead use a single loop and the string repetition operator "*":

# In[2]:

num_lines = int(input("Number of lines: "))
for i in range(num_lines):
    print("*" * (num_lines - i))


# ## Guessing Game 2.0
# Let's add functionality to the guessing game to allow a user to play the game as many times as they want. This will require an outer menu loop to keep the guessing game going until the user wants to quit, and an inner loop to guide the user to the correct answer.

# In[3]:

import random

def display_menu():
    '''

    '''
    print("\n**Welcome to the guess my number game!**")
    print("Please choose from the following options")
    print("1) View the game rules")
    print("2) Play the game")
    print("3) Quit")

def display_game_rules():
    '''

    '''
    print("The rules are fairly straightforward.")
    print("Guess a number and I will tell you if you are correct, too high, or too low")

def play_guessing_game():
    '''

    '''
    num_to_guess = random.randrange(1, 11)
    players_guess = 0
    correct = False

    while not correct:
        print("Please enter a number between 1 and 10 inclusive")
        players_guess = int(input())

        # a guess is either equal to, greater than, or less than
        if players_guess == num_to_guess: # BC 1
            print("Congrats, you guessed the number correctly")
            correct = True # exit loop
        elif players_guess > num_to_guess: # BC 2
            print("Your guess was too high")
        else: # players_guess < num_to_guess
            print("Your guess was too low")


def take_menu_action(choice):
    '''

    '''
    if choice == 1:
        display_game_rules()
    elif choice == 2:
        play_guessing_game()
    elif choice == 3:
        print("Thank you for playing")
    else:
        print("Not a valid menu option")

def main():
    '''

    '''
    choice = -1

    while choice != 3:
        display_menu()
        choice = int(input(">>"))
        take_menu_action(choice)

main()

'''
## MA12 Practice Problem
On a blank sheet of paper, write the following:
1. Your full name
1. Your TA name
1. MA #12

In pairs (or individually), solve the following problems. Each student needs to turn in their own paper to get credit for MA12.

### Problem 1
Write a program that prompts the user for an integer, `n`, representing a grid size. Using nesting loops, display a `n` by `n` grid of stars. Example:

```
Please enter a n value: 5
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

### Problem 2
Now, instead of stars, display numbers like the following example. Example:

```
Please enter a n value: 5
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
```
'''

num_lines = int(input("Number of lines: "))
for i in range(num_lines):
    for j in range(num_lines):
        print("*", end=" ")
    print()

for i in range(num_lines):
    for j in range(num_lines):
        print(i + 1, end=" ")
    print()


#files

'''
storing data
    many applications require storing and retreiving data outside of a program. Think off the many different applications you regularly use, do they utilize information that has been saved in some way?
        PC: your operating system stores all of your settings, files, and machine state for you
        banks: every customers transaction history is stored in massive databases in data warehouses
        games: your progress in a gme is stoed in a file
        search history:
        authentication

text files
    a simple way to store data is in a text file

    to process in a file, we typically take the following approach:
        1. open the file
        2. process the file
            read data (doesnt modify the file)
            write data (overwrite existing file)
            append data (retains existing information and adds new
            data)
        3. close the file

    opening a file
        open()

        file modes
            the first argument to open() is a string representing the path to the file and the second argument is the file opening mode

            1. 'r' for reading
                file must exist or you will get error
            2. 'w' for writing
                if the file does not exist, it is created
                if the file does exist, it is cleared
            3. 'a' for appending
                if the file does not exist, it is created
                if the file does exist, new data written to the file is added at the end of the file

        paths
            current directory: the directory, or folder, where your python script is running

            if a file you want to open is in a directory other than the current directory, you will have to specify its path

            there are two ways to specify a path:
                1. relative path: a path to a file or directory relative to the current directory
                2. absolute path: a path to a file or directory specified by its exact lcation on your file system

        closing a file
            close()

        processing a file
            reading from a file
                readline(): function to read in a single line in the file
                write(): function to write

ex:
    Algorithm:

        For each transaction
            Read in the purchase price from file
            Accumulate the total money spent so far
        Divide total money spent by total number of transactions
        Write the average transaction to file
'''
def read_transaction_price(in_file):
    '''

    '''
    # readline() returns a string, including the newline character
    price = in_file.readline()
    # we need to convert the string returned by readline() to a numeric value
    return float(price)

def compute_total_spent():
    '''

    '''
    total_spent = 0.0

    in_file = open("transactions.txt", "r")

    # read in all 5 transactions in the file
    for i in range(5):
        total_spent += read_transaction_price(in_file)

    # close the file before in_file goes out of scope
    in_file.close()

    return total_spent

total_spent = compute_total_spent()

avg_spent_per_transaction = total_spent / 5.0

out_file = open("avg_transaction.txt", "w")
out_file.write("On average, you spend %.2f per transaction" %(avg_spent_per_transaction))
out_file.close()


'''
MA13 Practice problems
(2 pts) Evaluate to True or False:
    7 % 2 == 3 or 12 // 10 == 2.2
    9 / 2 > 4 or -3 >= 0 and -5

(1 pt) Besides their name, what are the differences between a while loop and a for loop?

(3 pts) Construct a while loop that displays numbers in the range [3, 30] inclusive that are multiples of 3.

(4 pts) Construct a for loop that sums 10 randomly generated numbers in the range [4, 8] inclusive.
'''
