#Lists

'''
Lists
    list: sequence of items
        we declare a sequence of items as a list with hard brackets
'''
list_ints = [0, 1, 10, 20]
print(list_ints)

list_floats = [0.2, 0.4, 0.6, 1.0]
print(list_floats)

# types can be mixed in a list
list_numbers = [0, 0.0, 1, 1.0, -2]
print(list_numbers)

list_strings = ["cat", "dog", "bird"]
print(list_strings)

'''
list indexing
    list indicies are 0-based.

    we can index into a list to access a list item just like how we indexed into a string to get an individual character

list length
    we can use the len() function to determine the number of items

empty list
    a list has no items

nested lists
    lists in lists

lists are mutable
    we can change the items in a list

looping through list items
    we can use the in operator or indices to iterate through items in a list
'''

'''
list operators
    list concatenation
        use the '+' operator

    list repetition
        use the '*' operator

    list slicing
        use the ':' operator
'''

'''
tuples
    tuples are immutable lists

    they are declared as a comma seperated list, with or without parentheses
'''
my_tuple = "x", "y", "z"
print(my_tuple)
print(type(my_tuple))

# need a comma after a single element initialization
my_tuple2 = (1, )
print(my_tuple2)

# need a comma after a single element initialization
not_a_tuple = ("a")
print(not_a_tuple)
print(type(not_a_tuple))

# creating an empty tuple
empty_tuple = tuple()
print(empty_tuple)
print(type(empty_tuple))
