# Accessing global variables/expressions
count = 20
def increment():
# Adding the 'global' to the count defines it as a global variable.
    global count
    count += 2.5
    print(f"And the lucky number of the day is: {count}")

# Summon the function
increment()
increment()

# Access the global variable
print(f"And the winning number is... {count}!")
