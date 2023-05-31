
#Conditional Statements (if, elif, else):

"""
Python's if, else, and elif conditional statements let you modify the program's 
flow based on certain circumstances. These conditional statements are essential 
for Python programs to make decisions. They provide you the ability to develop logic 
that reacts differently based on multiple situations, which gives your code greater 
versatility and situational awareness.

"""


"""
If a condition is true, a block of code is 
then executed using the if statement. This enables you to do specific actions only 
under specified circumstances.

"""
# if

num = 10

if num > 0:
    print("The number is positive.")


"""
When used with the if statement, the else statement specifies an alternate code block to 
run when the if statement's condition is false. It enables you to manage circumstances where 
the requirement is not met and take appropriate action.

"""

# If, else

num = -5

if num >= 0:
    print("The number is non-negative.")
else:
    print("The number is negative.")
    
    
"""
The elif phrase, which stands for "else if," is employed to sequentially test many conditions. 
After the original if statement, it gives a mechanism to check for additional criteria. The accompanying
piece of code is executed if the if statement or any of the elif conditions that came before it evaluate 
to true. If the else block is present, it is run if none of the requirements are true.

"""

# if, elif, else

age = 25

if age < 18:
    print("You are underage.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
    


