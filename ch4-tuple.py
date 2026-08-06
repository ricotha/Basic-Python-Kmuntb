my_tuple = ()
print(my_tuple) # Output: ()

my_tuple1 = (1, 2, 3)
print(my_tuple1) # Output: (1, 2, 3)

my_tuple2 = ('a', 'b', 'c')
print(my_tuple2) # Output: ('a', 'b', 'c')

my_tuple3 = (1, 'a', 2, 'b', 3)
print(my_tuple3) # Output: (1, 'a', 2, 'b', 3)

# Accessing tuple elements
print(my_tuple1[0]) # Output: 1
print(my_tuple2[2]) # Output: c

# Tuple concatenation
my_tuple4 = (4, 5, 6)
combined_tuple = my_tuple1 + my_tuple4
print(combined_tuple) # Output: (1, 2, 3, 4, 5, 6)

# Tuple Methods
# Adding elements to a tuple is not possible since tuples are immutable. However, you can convert a tuple to a list, add elements to the list, and then convert it back to a tuple.
my_tuple1 = list(my_tuple1)  # Converts tuple to list
my_tuple1.append(4)  # Adds 4 to the end of the list
print(my_tuple1) # Output: [1, 2, 3, 4]
my_tuple1 = tuple(my_tuple1)  # Converts list back to tuple
print(my_tuple1) # Output: (1, 2, 3, 4)

# Removing elements from a tuple is also not possible since tuples are immutable. However, you can convert a tuple to a list, remove elements from the list, and then convert it back to a tuple.
my_tuple1 = list(my_tuple1)  # Converts tuple to list
my_tuple1.remove(4)  # Removes the first occurrence of 4
my_tuple1 = tuple(my_tuple1)  # Converts list back to tuple
print(my_tuple1) # Output: (1, 2, 3)

