# String
name = "John Doe"
message = "Hello, World!"


# Dictionary
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022
}


# Tuple
coordinates = (10, 20)
person = ("John", 25, "john@example.com")


# TALK ABOUT STACK AND QUEUE (LIFO & FIFO)


# List
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
print(fruits[0])  
print(fruits[-1]) 

fruits.append("orange")   
print(fruits) 
   
fruits = fruits + ["grape"] 
print(fruits) 


fruits.remove("banana") 
print(fruits) 

removed_fruit = fruits.pop(1)
print(fruits) 

del fruits[0] 
print(fruits) 


fruits = ["apple", "banana", "orange"]
print(len(fruits))  
print("banana" in fruits) 


# List Slicing

range_selection = fruits[1:3]        
print(range_selection) 



# LIST COMPREHENSION


K = [1, 2, 3, 4, 5]
Y = [x**2 for x in K]
print(Y)


names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)



#Concatenation

fruits = ["apple", "banana", "orange"]
colors = ["red", "yellow", "orange"]
combined = [(fruit, color) for fruit in fruits for color in colors]
print(combined) 



import random
random_numbers = [random.randint(1, 100) for _ in range(5)]
print(random_numbers)

num_steps = [x for x in range(0, 20, 2)]
print(num_steps)

evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)


# Unpacking
# Converting Tuple to List


# Adding and Updating Items in a Dictionary:
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

# Add a new key-value pair
student["university"] = "ABC University"

# Update an existing value
student["age"] = 21

