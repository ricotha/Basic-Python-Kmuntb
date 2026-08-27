# Part I- Importing Liberies
import math

# Part II- Defining Functions
def greet():
    print("Hello, World!")

def greet_with_name(name):
    print(f"Hello, {name}!")

def greet_with_name_and_age(name, age):
    print(f"Hello, {name}! You are {age} years old.")


def add_numbers(a, b):
    #local variable
    a += 1
    b += 1
    result = a + b
    return result

# Part III- Global Variables
a = 5
b = 10
result = 0
# Main code
result = add_numbers(a, b)
print(a)
print(b)
print(result)
# greet()
# greet_with_name("John")
# greet_with_name_and_age("Alice", 25)
# greet_with_name_and_age("Bob", 30)



# Interpreter
# Compiler
