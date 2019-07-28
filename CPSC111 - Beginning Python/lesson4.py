#Functions

'''
ex: write a program that computes your gradepoint average(gpa) after completion of three courses

    inputs:
        Grade point and number of credits for course 1
        Grade point and number of credits for course 2
        Grade point and number of credits for course 3

    outputs:
        Grade point average (GPA) Relevant formula: GPA = ((grade_point1 * num_credits1) + (grade_point2 * num_credits2) + (grade_point3 * num_credits3)) / total_num_credits

    algorithm:
        1. Get the grade points earned from each class
        2 .Get the credit hours for each class
        3 .Compute the credits hours earned
            weighted_credits = (grade_point1 * num_credits1) + (grade_point2 * num_credits2) + (grade_point3 * num_credits3)
        4. Compute the total number of credits
            total_num_credits = num_credits1 + num_credits2 + num_credits3
        5. Compute the average of the grade points
            gpa = weighted_credits / total_num_credits
        6. Display the results
'''

def gpa():
    class1 = float(input("Please enter the grade point for your computer science course: "))
    credits1 = int(input("Please enter the number of credits for your computer science course: "))
    class2 = float(input("Please enter the grade point for your math course: "))
    credits2 = int(input("Please enter the number of credits for your math course: "))
    class3 = float(input("Please enter the grade point for your science course: "))
    credits3 = int(input("Please enter the number of credits for your science course: "))

    weighted_credits = (class1 * credits1) + (class2 * credits2) + (class3 * credits3)

    total_num_credits = credits1 + credits2 + credits3
    gpa = weighted_credits / total_num_credits
    print(gpa)

'''
Functions
    function: a named sequence of statements that performs a computation. kind of like a mini program that solves a problem

    general rule:
        1 function = 1 task = 1 algorithm

Calling a function
    python accepts input arguments
        the inputs to the function

    you can use the word "return" to define the output parameters

Defining a Function
    a function defenition specifies the name of a function and the statements to be exectued when the function is called

    aspects to note:
        1. def is a keyword that lets python know you are about to declare a function
        2 .input parameters represent data coming into your function
        dont forget to put a colon after the last paren
        3. together, def and input parameters for the function header
        4. the rest of the function is called the function body and should be indented 4 spaces

Lets revisit the calculating GPA program using functions
'''
def get_credits(course_name):
    '''
    Prompts the user for the number of credits for a course.
    '''
    print("Please enter the number of credits for %s: " %(course_name))
    num_credits = int(input())
    return num_credits

def compute_weighted_credits(gp1, gp2, gp3, num_credits1, num_credits2, num_credits3):
    '''
    Computes the weighted credits for three courses.
    '''
    weighted_credits = (num_credits1 * gp1) + (num_credits2 * gp2) + (num_credits3 * gp3)
    return weighted_credits

def sum_credits(credits1, credits2, credits3):
    '''

    '''
    total_credits = credits1 + credits2 + credits3
    return total_credits

def compute_gpa(weighted_credits, total_num_credits):
    '''
    Averages the weighted credits earned by the total number of credits taken.
    '''
    gpa = weighted_credits / total_num_credits
    return gpa

def display_gpa(gpa):
    '''
    Displays the final gpa to the user.
    '''
    print("Your GPA is: %.2f" %(gpa))

# get grade point and credit hours for each class
gp1 = get_grade_point("computer science")
num_credits1 = get_credits("computer science")

gp2 = get_grade_point("math")
num_credits2 = get_credits("math")

gp3 = get_grade_point("karate")
num_credits3 = get_credits("karate")

# compute the weighted credit hours earned
weighted_credits = compute_weighted_credits(gp1, gp2, gp3, num_credits1, num_credits2, num_credits3)

# compute the total number of credits earned
total_num_credits = sum_credits(num_credits1, num_credits2, num_credits3)

# copute the average of the grade points
gpa = compute_gpa(weighted_credits, total_num_credits)

# display the results to the user
display_gpa(gpa)


'''
MA5 Practice Problem
    1. Solve practice problems 2 and 3 from L3-2 without using functions.
    2. Re-solve practice problems 2 and 3 from L3-2 using functions. Define functions for:
        Getting user input
        Computing results
        Display the results
'''

#more functions

'''
Why use functions?
    break a large, complex solution into logical units
        individual members of a programming team can work on each unit independently
    procedural abstraction
        the calling function need not be aware of the details of how a function works
    reuse
        functions allow us to package up a well-designed solution into a bite-size chunk that can be resused over and over
    testing
        allows for more efficient testing and bug resolution

Function testing
    each function itself is a small program
    ideally its a self-contained "black box", meaning it does not manipulate global variables

how functions are executed
    when a function is called, memory for local variables is allocated
    memory is released upon completion of function execution

Scope
    scope of a name: region of a progam where a particular meaning of a name is visible or can be referenced

    global variables
        variables declared outside of a function
        in general, there a bad idea and we should try to avoid using them

    local variables
        parameter variables and variables declared inside a function

Body-less function
    you can define a function without adding a body by simply placing the reserved word "pass" in the body
'''
