"""
A function is a block of code that performs a specific task. 
It takes input, processes it, and produces output. Functions 
help in organizing code into reusable blocks, making the code 
more modular and easier to understand.

"""
# CASE 1
def greet():
    print("Hello, world!")

greet()


# CASE 2
def greet(name):
    print("Hello, " + name + "!")

greet("Great")


# CASE 3
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print(result)


# CASE 4
def greet(name="world"):
    print("Hello, " + name + "!")

greet()

greet("Great")

# CASE 5
def greet(first_name, last_name):
    print("Hello, " + first_name + " " + last_name + "!")

greet(last_name="Smith", first_name="John")








#ADVANCE 

# CASE 6
def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

user_email = input("Enter your email: ")
if is_valid_email(user_email):
    print("Valid email")
else:
    print("Invalid email")


# CASE 7

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Moderate"
    else:
        return "Strong"

user_password = input("Enter your password: ")
strength = check_password_strength(user_password)
print("Password strength:", strength)


# CASE 8

def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

user_email = input("Enter your email: ")
if is_valid_email(user_email):
    print("Valid email")
else:
    print("Invalid email")

# CASE 9

def reverse_string(input_str):
    return input_str[::-1]

def is_palindrome(input_str):
    return input_str == reverse_string(input_str)

word = "radar"
if is_palindrome(word):
    print(word + " is a palindrome.")
else:
    print(word + " is not a palindrome.")


# CASE 10
