""" 
You may repeat a piece of code several times with the help of loops, which are a 
crucial component of programming. The for loop and the while loop are the two 
types of loops available in Python.

When you know how many times you want to loop through a list of items or a sequence,
you use the for loop. It runs the block of code connected to the loop while iterating
over each element in the sequence or range. To iterate through lists, tuples, strings,
and other iterable objects is a popular practice.


Contrarily, you use a while loop to repeatedly execute a piece of code as long as a 
particular condition is True. The code block is kept running until the condition is 
false. Before beginning each loop iteration, the condition is assessed.

Loops are effective programming structures that let you easily automate complicated 
processes, process massive volumes of data, and handle recurring activities. You may
make programs that are more dynamic and adaptable by using them frequently in 
conjunction with conditional expressions.

To prevent infinite loops, it's critical to make sure the condition will finally 
turn False while utilizing loops. Statements like break and continue, which give 
you more control over the loop's progression, can be used to modify how the loop runs.

"""
# Loops (for loop):
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

#Loops (while loop):
count = 0

while count < 5:
    print("Count:", count)
    count += 1


#Branching (break statement):
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        break
    print(num)

#Branching (continue statement):
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        continue
    print(num)
