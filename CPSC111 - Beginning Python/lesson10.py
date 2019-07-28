#more file i/o and Practice

'''
the file "cursor"
    when you open a file for reading, the curesor marking the current position at which to read from starts at the begining of the file (position 0)

    as readlines() is called, the cursor moves through the file

    to mobve the cursor back to the beginning of the file, you can either close the file and re-open it for reading

    ex.
'''
in_file = open("transactions.txt", "r")

print("File cursor is at the beginning of the file.")
for line in in_file.readlines():
    print(line)

in_file.close()
in_file = open("transactions.txt", "r")

print("File cursor is at the beginning of the file.")
transaction = in_file.readline()
print(transaction)

'''
removing leading and trailing whitespace characters
    we can remove white space characters by calling strip()

    ex
'''

in_file = open("transactions.txt", "r")

# read data from the file advances the cursor by a certain number of bytes,
# depending on the number of characters in the line
transaction = in_file.readline()

# repr() displays all characters in a string. we use it see the newline character as \n
print("First line: ", repr(transaction))
in_file.close()
print("First line stripping leading/trailing whitespace characters: ", repr(transaction.strip()))

'''
revisiting print()
    ex
'''
# format string and placeholders
print("Integer: %d, Float: %f, Float with 1 decimal: %.1f, String: %s" %(7, 8.4898899, 3.14, ":)"))

# arguments displayed separated by spaces
print(4, 5.5, ":P", 8)
# specifying the delimiter between arguments (a comma and a space)
print("A comma", "separated", "list", sep=", ")

# specifying the string concatenated to the end
print("A string without the added newline character", end="")
print("This sentence runs into the previous", end="!\n")

# https://docs.python.org/3/library/string.html
print("An {} form of placholders {:.1f}. You can also use keywords {name}".format("alternative", 9.99, name="cpts111"))

# alternative way to write to a file using print() instead of write()
outfile = open("out_demo.txt", "w")
print("Writing this output via print()", file=outfile)
outfile.close()

'''
common errors when working with files
    -using the wrone file handle to refer to  file
    -opening a nonexistent file for reading
    -Using a file object whose cursor is at the end of the file
    -Opening a file for reading or writing without the appropriate access rights
    -Opening a file for writing when no disk space is available
    -Opening a file for writing ("w") when the users wants to preserve the previous ---contents of the file ("w" discards all contents of file)
        -Use ("a") to append instead
'''

#strings

'''
review of strings
    string: sequence of characters

    string concatenation
        use the '+' operator

    string and for loops
        for <item> in <sequence>:
            <body>

    string indexing
        the word python is organized as follows
         ___________________________________
        |index:     | 0 | 1 | 2 | 3 | 4 | 5 |
        |Character: | p | y | t | h | o | n |

        we can access a single character by using the indexing notation

    string length
        we can find out the length of a string, meaning the number of characters in the string by using len()

    the empty string
        a string with no characters

    strings and while loops 
        we can use a while loop and the built-n len() function to display individual characters of a string

    string slicing
        we can use the ':' operator to select a slice of string: <string variable>[start_index:end_index + 1]

Immutability of strings
    strings are immutavle, meaning they can't be changed. this means we cannot re-assign a character of a string
'''
