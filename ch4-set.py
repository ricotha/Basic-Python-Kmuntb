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
