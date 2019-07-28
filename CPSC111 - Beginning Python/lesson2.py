#Arithmetic

'''
'+' -> addition
'-' -> subtraction
'*' -> multiplication
'/' -> floating point division
'//' -> integer division
'**' -> exponentiation

examples!!
'''

print(2 ** 3 ** 2)
print(4 ** 2 / 4)
print(4 ** (2 / 4))

# when making an expressions with different types, the result will use the more
# precise data type
# examples!!

result = 0
op1_int = 5
op2_int = 42
op1_float = 5.5

# integer expression
result = op1_int + op2_int
print(result, type(result))

# mixed expression
result = op1_int + op1_float
print(result, type(result))

result = int(op1_int + op1_float)
print(result, type(result))


'''
CHANGING TYPES
two kinds of conversions:
    implicit
    explicit
'''

#implicit
num1 = 12 #int
num2 = 0.0 #float
num2 = num1 #num2 is now an int
print(num2, type(num2))

#explicit
num1 = 1.7 # float
num1 = int(num1)
print(num1, type(num1))

#manipulation
x = 5.87
print(int(x)) # truncates
print(round(x)) # rounds to nearet integer
print(round(x, 1)) # rounds to one decimal place


#FORMATTING NUMBERS
x = 3
y = 2.17
# outputs 2 spaces before the 3 and 2 spaces before the 2.2
print("x is%3d. y is%5.1f." %(x, y))

a = 504
b = 302.558
c = -12.31
print("%5d%11.2f%9.1f" %(a, b, c))
