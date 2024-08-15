# Craft a global counter
rego_counter = 50000
def student_rego():
    global rego_counter # Make use of this counter

    #Generate the Registration ID using the corrent counter value
    rego_id = rego_counter
    rego_counter += 1 # Increment counter for next registration
    
    # Inputted info from the user
    date = input("Please enter your rego date (dd/mm/yyyy): ")
    student_id = input("Please enter your Student ID: ")
    student_name = input("Please enter your name: ")
    course_name = input("Please enter the course name: ")

    # Return the collected info and registration data
    return date, student_id, student_name, course_name, rego_id

# Summon the functions and retrieve the data!
date, student_id, student_name, course_name, rego_id = student_rego()

# Display the info on the terminal
print("Printing Student Registration Information:")
print(f"Date: {date}")
print(f"Student ID: {student_id}")
print(f"Student Name: {student_name}")
print(f"Course Name: {course_name}")
print(f"Registration ID: {rego_id}")

# Summon the functions!
student_rego()