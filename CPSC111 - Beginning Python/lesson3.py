#Errors and Practice

'''
3 types:
  1. Syntax errors - where the code violates syntax rules for a proper python program
    - detected at compile time
    - program will not run unless they are corrected
    - ex:
      -undeclared identifiers
      -invalid identifiers
      -failure to close a comment or string properly
      -incorrect indentation
  2. Runtime errors
    - causes a program to "crash": an error is reported, and control is turned over to the operating system
    - ex:
      -division by zero
      -getting into an infinite loop, which may ultimately cause a stack overflow
   3. Logic errors
     - cause the program to compute incorrect results
     -often go unnoticed

'''


'''
MA3 practice problems
    Label each of the following as either "Python reserved keyword", "standard identifier", or "other valid identifier":
        int: standard
        PI: other
        if: reserved
        main: other
        while: reserved
        high_score: other

    How should you read the statement: temp_value = old_value + new_value?
        "temp_value" equals "old_value" plus "new_value"

    Which Python data type would be best to represent the following? For each blank, you may list int, float, or str only.
        Gender: str
        Average of 10 numbers: float
        Number of students in CptS111: int
        Price of a gallon of milk: float
'''

#Modules and Practice

'''
MA4 Practice Problems
    What are the three kinds of programming errors? Can you give an example of each?
        A. syntax error
        B. run-time error
        C. logic error

    Rank the order of precendence for the following C operators (1 is the highest precendence and 5 is the lowest)
        + # binary addition
        - # unary minus (e.g. negation)
        % # modulus
        = # assignment
        () # parentheses
    Evaluate each of the following equations and determine the resultant data type:
        4 / 12 =
        4 // 12 =
        4 % 12 =
        7 // 4 =
        9.0 / 4.0 =
        3 / 0 =
        3.0 % 1 =
        16 % 0 =
        3 % 5 =
        9 % 5 =
        2 * 4 ** 2 =
        2 ** 4 ** (2 / 4) =
    Given y = m % n, what are the possible values of y?

    Write the following equation as a Python arithmetic statement: $$q=\frac{kA(T_1-T_2)}{L}$$

    Show the output displayed by the following program when the data entered are 12 for m and 0 for n:
        m = int(input("Enter an integer> "))
        n = int(input("Enter an integer> "))
        m = m + 5
        n = 3 * n
        print("m = %d\nn = %d\n" %(m, n))
'''

'''
Python Modules
    module: a file that contains a collection of related variables and functions

    you must import all of the modules before you can use them in your code

Math Functions
    the math module includes many common mathematical functions

    common functions:
        fabs() for absolute values
        ceil() for computing the ceiling of a number
        floor() for computing the floor of a number
        cos() for cosine function
        sin() for sine function
        tan() for tangent function
        pow() for raising a number to its power
        log() for logarithms (see also log2() and log10()
        sqrt() for computing square roots

Turtle Graphics
    used for doing GUI stuff

Software development method
    six basic steps:
        1. specify problem requirements
        2. analyze the problem
        3. design an algorithm to solve the problem
        4. implement an algorithm
        5. test and verify the completed program
        6. maintain and update the program
'''


'''
Practice Problems
    1. Write a program to compute the total price for a purchase after sales tax.

        example output:
        Please enter the purchase price: 9.00
        Please enter the sales tax as a percent (%): 7.8
        Total purchase price after tax: $9.70
'''

def sales_tax():
        purchase = float(input("Please enter the purchase price: "))
        tax_percent = float(input("Please enter the sales tax as a percent (%): "))

        tax = purchase * (tax_percent / 100.0)
        purchase += tax

        print("Total purchase price after tax: $%.2f" %(purchase))

'''
    2. write a program that calculates mileage reimbursement for a salesperson at the rate of $.35/mile

        example output:

        MILEAGE REIMBURSEMENT CALCULATOR
        Please enter the beginning odometer reading: 13505.2
        Please enter the ending odometer reading: 13810.6
        You traveled 305.4 miles. At $0.35 per mile, your reimbursement is $106.89
'''

def mileage_reimbursement():
    print("MILEAGE REIMBURSEMENT CALCULATOR")
    odo_begin = (float(input("Please enter the beginning odometer reading: ")))
    odo_ending = (float(input("Please enter the ending odometer reading: ")))

    traveled = odo_ending - odo_begin
    reimbursment = traveled * .35
    print("You traveled %.1f miles. At $.33 per mile, your reimbursement is $%.2f" %(traveled, reimbursment))

'''
    3. write a program that takes the values for m and n as input and displays the values of the Pythagorean triple generated by the formulas above

        example output:
            Please enter a m value: 4
            Please enter a n value: 2
            Pythagorean triple: 12^2 + 16^2 = 20^2
'''

def pythagorean():
    m = int(input("Please enter a m value: "))
    n = int(input("Please enter a n value: "))

    side1 = m**2 - n**2
    side2 = 2 * m * n
    hyp = m**2 + n**2

    print("Pythagorean triple:%d^2 + %d^2 = %d^2" %(side1, side2, hyp))
