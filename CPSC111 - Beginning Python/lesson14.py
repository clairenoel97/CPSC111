#binary

# the decimal (base 10) number system we use is a positional number system using digits 0 - 9

'''
binary
    binary is a positional number system

    binary only uses the digits 0 and 1. each digit in a binary number such as 1011
     _______________________
    | 2^3 | 2^2 | 2^1 | 2^0 |
    |  1  |  0  |  1  |  1  |

    1 * 2^3 + 0 *2^2 + 1 * 2^1 + 1 * 2^0 = 11


binary to decimal
    to convert a binary number to decimal:
        for each bit of the binary number:
            if the bit is a one, add 2^i to the accumulated sum where i is the position of the bit
'''

def binary_to_decimal(binary):
    '''

    '''
    decimal = 0
    highest_power_two = len(binary) - 1

    for i in range(len(binary)):
        digit = int(binary[i])
        decimal += digit * 2 ** (highest_power_two - i)

    return decimal

print(binary_to_decimal("1010101"))


'''
decimal to binary
    1. identify the largest power of 2 in the decimal number 2^N
    2. for each power of 2: 2^N, 2^N-1,..., 2^0
    3. if the power of 2 goes into the number evenly
        place a 1 at the powers position
        subtract the power of 2 from the number
    4. else
        place a 0

'''
def decimal_to_binary(decimal):
    '''

    '''
    binary = ""
    highest_power_two = int(math.log(decimal, 2)) # compute highest_power_two with log base 2(decimal)

    for N in range(highest_power_two, -1, -1):
        power_two = 2 ** N
        if decimal // power_two > 0: # check is power_two goes into the number evenly
            binary += "1"
            decimal -= power_two
        else:
            binary += "0"

    return binary

print(decimal_to_binary(94))


#Dictionaries

'''
dictionaries
    dictionary: a list with keys as indices
        keys can be integers, strings, file objects, etc

        keys cannot be lists

        declare with curly braces

compatible dictionary data types
    keys
        can be integers, strings, files, tuples, etc.....not lists
    values
        can be any type

dictionary indexing
    we can access an item via a key using hard brackets []

adding key-value pairs
    dictionaries are mutable, we can add key-value pairs to the dictionary using hard brackets []

dictionary length with len()

existence of a key
    we can also text if a key is valid key in the dictionary with the 'in' keyword

looping through a dictionary
    we can traverse a dictionary easily with a for loop that walks through each key in the dictionary



ex:
'''
# Suppose we want to keep track of the frequency of letters in a word. For example, the word "hello" has 4 letters with the following frequencies:
#
# h: 1
# e: 1
# l: 2
# o: 1
# Let's write a program to prompt the user to enter a word. Our program will tell the user the frequency of each letter in the word. We could solve this problem with either a list or a dictionary:
#
# List solution
# Create a list with 26 zeros
# Write a function to convert a letter into an integer in the range [0-25] to index into the list. We can do this with the ord(<character>) function and ASCII codes...
# Walk through the word and increment the corresponding list position for each letter
# Convert the index of non-zero list entries back to characters using char(<integer>) to print out the histogram results
# Dictionary solution
# Create an empty dictionary
# Walk through the word and add the letter to the dictionary with a count of zero if the letter is not already a key, increment otherwise.
# The dictionary solution lends itself more suitable to this problem because we do not have to allocate space for all letters ahead of time and we don't have to perform a character to integer conversion to index into the data structure.

def compute_letter_frequencies(word):
    '''

    '''
    histogram = {}

    for letter in word:
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram[letter] = 1
    return histogram

print(compute_letter_frequencies("hello"))
print(compute_letter_frequencies("mississippi"))
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
{'i': 4, 'm': 1, 'p': 2, 's': 4}

#Compared to the list solution:


def letter_to_index(letter):
    '''

    '''
    ascii_val = ord(letter)
    index = ascii_val - ord('a')
    return index

def index_to_letter(index):
    '''

    '''
    ascii_val = index + ord('a')
    letter = chr(ascii_val)
    return letter

def compute_letter_frequencies_list(word):
    '''

    '''
    histogram = [0] * 26

    word.lower()
    for letter in word:
        index = letter_to_index(letter)
        histogram[index] += 1
    return histogram

def pretty_print(histogram):
    '''

    '''
    for i in range(len(histogram)):
        if histogram[i] != 0:
            letter = index_to_letter(i)
            print("%s: %d" %(letter, histogram[i]), end=" ")
    print("")

histogram = compute_letter_frequencies_list("hello")
pretty_print(histogram)
