#Introduction

'''
What is Computer Science?
    computer science is the study of computers and computational systems with a focus on algorithms and problem solving

    an algorithm: is a sequence of instructions that solves a problem
    problem solving: is formulating problems and designing creative, clear, and accurate solutions

What can computers do?
    6 fundamental operations:
        1. accept input
        2. produce output
        3. assign a value to a variable (store data)
        4. arithmetic (math)
        5. compare and branch (conditionals)
        6. repeat a set of instructions (loops)

Algorithms
    a sequence of instructions is an algorithm if it meets the following criteria
        - well ordered instructions
        - unambiguous instructions
        - computable instructions
        - produces a result
        - doesn't run forever

    why are they so important?
        -we can automate a solution
        -we can also repear a solution to a problem

High-level programming languages
    programming languages are a medium between natural languages(english, spanish, etc) and binary(0's and 1's).
'''

'''
Getting started with Python

Python is an interpreted language, meaning as long as the machine has the Python
interpreter installed, Python can be run


INTEGRATED DEVELOPMENT ENVIRONMENTS (IDE)
an IDE is a program we use to write other programs. It conveniently combines
editing of source code with running you programs


EX: write a program that computes the volume of a cone
    formula: (pi*r^2)(h/3)

    what info do we need?
        the radius
        the height

    data requirements:
        input of the base and height
'''

def cone_volume():
    print("Please enter the radius of the cone's base: ")
    radius = float(input())
    print("Please enter the height of the cone:")
    height = float(input())

    volume = (1/3) * 3.14 * (radius ** 2) * height

    print("The volume of your cone is: %.2f" %volume)

cone_volume()


# PYTHON BASICS
# this is a comment
# used to describe a useful statement in the code

'''
this is a block comment
'''

'''
Reserved words
    python has reserved several identifiers as keywords that have a special meaning avout the nature of the program.

    you can youse these as user-identifiers in your program

standard identifiers
    represent names of built-in variables (data) and functions (operations) in Python

    ex: print(), input()

user-defined identifiers
    memory cells to store data (variables) that are named by the programmer for computations

DATA TYPES
a data type is a set of values and a set of opterations on those values

integer, float, string,
'''
