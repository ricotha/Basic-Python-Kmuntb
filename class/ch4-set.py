# Set
my_set = {}
print(my_set) # Output: {}

my_set1 = set([1, 2, 3, 4, 5, 6])
print(my_set1) # Output: {1, 2, 3, 4, 5, 6}

my_set2 = set([1, 2, 2, 3, 4, 5, 6])
print(my_set2) # Output: {1, 2, 3, 4, 5, 6}

# Accessing set elements
# Sets are unordered collections, so you cannot access elements by index. However, you can iterate

for item in my_set1:
    print(item) # Output: 1 2 3 4 5 6 (order may vary)

# Adding elements to a set
my_set1.add(7) # Adds 7 to the set
print(my_set1) # Output: {1, 2, 3, 4, 5, 6, 7}

# Removing elements from a set
my_set1.remove(7) # Removes 7 from the set
print(my_set1) # Output: {1, 2, 3, 4, 5, 6}

# Set operations
# Union
# Intersection
# Difference
# Symmetric Difference


# List
# my_list = [1, 2, 3, 4, 5]
# my_list[1] = 20 # Modifying an element
# for i in range(len(my_list)): #(init, condition, increment)
#     print(my_list[i]) # Output: 1 20 3 4 5

# # Methods to add and remove elements from a list
# my_list.append(0) # Adds 6 to the end of the list
# my_list.insert(0, 0)
# my_list.remove(0) # Removes the first occurrence of 0 from the list
# my_list.pop() # Removes the last element from the list
# my_list
# del my_list

# Tuple
my_tuple = (1, 2, 3, 4, 5)
list(my_tuple) # Converts the tuple to a list
tuple(my_tuple) # Converts the list back to a tuple

# Set
my_set = {1, 2, 3, 4, 5}

# Dictionary