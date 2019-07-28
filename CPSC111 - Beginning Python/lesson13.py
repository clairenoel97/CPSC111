# list methods

'''
list methods
    append(): add an item to the end of a list
    extend(): is similar to append(); however, extend() takes a list as an agrugment and adds each item to the list
    sort(): sorts the list in ascending order
'''

'''
deleting itemds in a list
    single item deletes
        -when you know the index of the item to delete
            item_removed = pop(<index>)
        -when you know the value of the item to delete
            remove(<item>)

    del keyword and multiple items deletes
'''

'''
join() (string method)
    we can turn a list of strings into a string with the join() method

    we need to specify a delimiter string to use to concatenate the individual strings in a list into single string

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

'''
list() (function)
    to convert the string back into a list
'''
my_string = "cpts111"
my_list = list(my_string)
print(my_list)

'''
split()
    breaks a string into pieces at each delimiter and the pieces are returned as a list
'''
sentence = "hello how are you"
pieces = sentence.split(" ")
print(pieces)




#advanced lists

'''
aliasing
    phenomenon when two objects refer to the same object
'''

'''
list arguments
    when a list is paddes as an agrument to a function, the function parameter variable is a reference to the list, making it aliased

returning lists
    functions can return lists 
