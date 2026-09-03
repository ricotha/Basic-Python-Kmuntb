# File Handing

# Open a file 
file = open("test.txt", "w")  # Open a file in write mode

# Read the file 
# print(file.read())  # Read the contents of the file
print(file.readable())  # Check if the file is readable
print(file.readable())  # Check if the file is readable
print(file.readable())  # Check if the file is readable

for line in file:
    print(line.strip()) # Print each line in the file
                        # strip() method removes any leading and trailing whitespace characters from the line

# CLose the file
file.close()  # Close the file

# Write to a file
file = open("test.txt", "w")  # Open a file in write mode
file.write("This is a test file.\n")  # Write another string to the file
file.close()  # Close the file 

with open("test.txt", "w") as file:  # Open a file in write mode using 'with' statement
    print(file.read())  # Read the contents of the file

import os  # Import the os module

if os.path.exists("test.txt"):  # Check if the file exists
    os.remove("test.txt")  # Remove the file
else:
    print("The file does not exist")  # Print a message if the file does not exist
