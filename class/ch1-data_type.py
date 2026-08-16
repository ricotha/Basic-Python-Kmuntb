# #Data Types

# #Integer
# age = 25
# print(type(age)) 

# #Float
# price = 19.99
# print(type(price))

# #String
# name = "John"
# print(type(name))

# #Boolean
# is_student = True
# print(type(is_student))

# #Data Structures
# #ist = [1, 2, 3, 4, 5]
# #ist = [1, 2, 3, 4, 5]
# # print(type(list))
# # set = {1, 2, 3, 4, 5}
# # print(type(set))
# # tuple = (1, 2, 3, 4, 5)
# # print(type(tuple))
# # dictionary = {"name": "John", "age": 25, "is_student": True}
# # print(type(dictionary))

#Operators
#Assignment Operators (=)
# x = 5
# print(x)  # Output: 5

# #Arithmetic Operators (+, -, *, /, %, **, //)
# a = 10
# b = 3
# print(a + b)  # Addition
# print(a - b)  # Subtraction
# print(a * b)  # Multiplication  
# print(a / b)  # Division
# print(a % b)  # Modulus
# print(a ** b)  # Exponentiation
# print(a // b)  # Floor Division


# #Comparison Operators (==, !=, >, <, >=, <=)
x = 10
y = 5
print(x == y)  # Equal to / Returns True
print(x != y)  # Not equal to / Returns True
print(x > y)   # Greater than / Returns True
print(x < y)   # Less than / Returns False
print(x >= y)  # Greater than or equal to / Returns True
print(x <= y)  # Less than or equal to / Returns False

# #Logical Operators (and, or, not)
p = True
q = False
print(p and q)  # Logical AND / Returns False
print(p or q)   # Logical OR / Returns True
print(not p)    # Logical NOT / Returns False

# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# print("Sum:", int(num1) + int(num2))
 
#String - Data Types
str1 = "Learning Python";
print(type(str1))  
print(len(str1))        # Count characters

a = 9.0      #Float
a = str(a)   # Float -----> string
print(type(a))  

print("Python" in str1) #True
print("England" in str1) #False

#String is a List/Array
str2 = "We are I-BIT program."
print(str2[0])  # W
print(str2[0:8])  
print(str2[0:12]) 
print(str2[:12])
print(str2[3:])

print(str2[-1])

#String Manipulation functions
str3 = "Hello, Human."
print(str3.upper())  # Convert to uppercase
print(str3.lower())  # Convert to lowercase
print(str3.strip())  # Remove leading and trailing whitespace
print(str3.replace("H", "X"))
print(str3.split(","))  # Split the string into a list based on the comma delimiter

str4 = str3 + ",We are I-BIT"
print(str4)  # Concatenation

age = 25
txt = "Jhon Smith"
print(txt,"I am", age , "years old.")  # Concatenation with variable
print(f"{txt} I am {age} years old.")  # Using f-string for formatting

str5 = "Learn Python"
#Find
print(str5.find("Py"))  # Returns the index of the first occurrence of "Python"