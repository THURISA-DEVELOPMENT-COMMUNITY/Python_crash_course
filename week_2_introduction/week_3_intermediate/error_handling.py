'''
SyntaxError, IndentationError, NameError, TypeError, ValueError,
IndexError, KeyError, FileNotFoundError,ImportError, ZeroDivisionError,
AttributeError, IOError, RuntimeError, KeyboardInterrupt, OverflowError,
MemoryError,PermissionError, AssertionError

'''


# Handling all exceptions

try:
    print("hello world!")
except:
    print("Error!")


# Handling specific exceptions
try:
    print("hello world!")
except ValueError:
    print("Error!")
except FileNotFoundError:
    print("Error!")




# Handling multiple exceptions

try:
    print("hello world!")
except (ValueError, FileNotFoundError):
    print("Error!")



# The else block

try:
    print("hello world!")
except ValueError:
    print("Error!")
else:
    print("First 2 steps faild!")



# The finally block

try:
    print("hello world!")
except ValueError:
    print("Error!")
finally:
    print("Nothing can stop me")


# Raising exceptions
x = int(input("Enter a number: "))
if x < 0:
    raise ValueError


# Application 

try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
