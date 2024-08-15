# Accessing global variables/expressions

total_sum = 0

# Define your add_to_sum by making total_sum into a global variable
# and adding on the same total by using += which gives the increased sum
def add_to_sum(num):
    global total_sum
    total_sum += num
# The (num) acts as an ID for add_to_sum. It can be called anything.

# Remember to add the f at the beginning, as it IDs the function values
# below, otherwise it will only appear as {total_sum} on the terminal
def display_sum():
    print(f"And your total is: {total_sum}")

# Summon the functions
add_to_sum(4)
add_to_sum(14)
add_to_sum(40)
display_sum()

