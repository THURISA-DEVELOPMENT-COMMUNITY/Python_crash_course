# Opening a File
file = open("test.txt", "r")

# Read the entire file
content = file.read() 

# Read a single line 
line = file.readline()  

# Read all lines and return a list
lines = file.readlines()  


# Writing to a File
file = open("test.txt", "w")
file.write("Hello, World!")

# Appending to a File
file = open("filename.txt", "a")
file.write("New content")



# Closing a File
file.close()

'''
Alternatively, you can use the {with} statement,
which automatically closes the file when you're done.
'''

with open("filename.txt", "r") as file:
    content = file.read()



# Error Handling

try:
    file = open("filename.txt", "r")
    # Perform file operations
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
