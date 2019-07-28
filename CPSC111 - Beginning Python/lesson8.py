#iteration with while loops

'''
Recall
    3 kinds of statements
        1. sequential: the ability to execute a series of instructions
        2. conditional: the ability to execute an instruction contingent upon some condition
        3. iterative: the abiliy to execute one or more instructions repeatedly

when is a loop needed?
    are any steps repeated?
        no: then no loop required
        yes: use a loop, simple as that

the while loop
    while <test>:
        <body>

    test is a boolean condition and body contains indented code that progresses towards the boolean condition testing
    if the test is false, then you can exit the loop
'''

#iteration and for loops

'''
random numbers
    to generate random numbers, we need to import the 'random' module. then, we can call either function to generate the random number
        1. randrange(start, stop) to generate a random number in the range 'start' to 'stop' - 1
        2. randint(start, stop) to generate a random number in the range 'start' to 'stop'

the for loop
    in addition to while loops, python has another type of loop.

    for <item> in <sequence>:
        <body>

    where sequence contains a finite number of items to be iterated through. if sequence is not finit, then we have an infinite loop

while or for loop
    when to use which loop? each loop construct lends itself more suitable for certain tasks

    for loops:
        iterating through sequences
            using range()
            files
            strings
            lists
            dictionaries
            when we know the number of times we want to run our loop

    while loops:
        prompting the user for input
        menus
        when we don't know the number of times we want to run our loop 
'''
