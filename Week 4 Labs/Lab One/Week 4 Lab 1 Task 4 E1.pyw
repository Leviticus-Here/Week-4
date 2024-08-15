# One function calls another to take the result and do further processing

def add(a, b):
    return a + b

def multiply(x, y):
    return x + y

# The add_result combines the first two numbers first, then the 
# multiply_result multiplies the two first numbers with a third number
# where the return command displays the end total of all three numbers.
def add_then_multiply(a, b, c):
    add_result = add(a,b)
    multiply_result = multiply(add_result,c)
    return multiply_result

# Add in an ID, then with your function, choose two numbers to add, then
# another to multiply the first two numbers together.
total= add_then_multiply(25,17,4)
print(total)