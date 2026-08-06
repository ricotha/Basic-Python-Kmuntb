# # List data type
# my_list =[]
# my_list1 = [1, 2, 3, 4, 5]
# my_list2 = ['a', 'b', 'c', 'd', 'e']
# my_list3 = [1, 'a', 2, 'b', 3]

# #Accessing list elements
# print(my_list1[0]) # Output: 1
# print(my_list2[2]) # Output: c
# print(my_list3[4]) # Output: 3

# print(my_list1[-5]) # Output: 1

# # for loop to iterate through a list
# for item in my_list1:
#     print(item) #Output: 1 2 3 4 5

# for i in range(len(my_list1)):
#     print(my_list1[i]) #Output: 1 2 3 4 5

# # List methods
# my_list1.append(6) # Adds 6 to the end of the list
# print(my_list1) # Output: [1, 2, 3, 4, 5, 6]
# my_list1.insert(2, 2.5) # Inserts 2.5 at index 2
# print(my_list1) # Output: [1, 2, 2.5, 3, 4, 5, 6]

# # Removing elements from a list
# my_list1.remove(2.5) # Removes the first occurrence of 2.5
# print(my_list1) # Output: [1, 2, 3, 4, 5, 6]

# my_list1.pop(2) # Removes the element at index 2
# print(my_list1) # Output: [1, 2, 4, 5, 6]

# # List slicing
# my_list1 = [1, 2, 3, 4, 5, 6]
# print(my_list1[1:4]) # Output: [2, 3, 4]
# print(my_list1[:3]) # Output: [1, 2, 3]
# print(my_list1[3:]) # Output: [4, 5, 6]
# print(my_list1[:]) # Output: [1, 2, 3, 4, 5, 6]

# # List concatenation
# my_list9 = [7, 8, 9]
# combined_list = my_list1 + my_list9
# print(combined_list) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # List repetition
# repeated_list = my_list1 * 2
# print(repeated_list) # Output: [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

# # List comprehension
# my_list10 = [x**2 for x in range(1, 6)]
# print(my_list10) # Output: [1, 4, 9, 16, 25]

# # List copying
# my_list11 = my_list1.copy()
# print(my_list11) # Output: [1, 2, 3, 4, 5, 6]
# my_list11.append(7)
# print(my_list11) # Output: [1, 2, 3, 4, 5, 6, 7]
# print(my_list1) # Output: [1, 2, 3, 4, 5, 6] (original list remains unchanged)  

# my_tuple = (1, 2, 3)
# my_list_from_tuple = list(my_tuple)
# print(my_list_from_tuple) # Coonverts tuple to list, Output: [1, 2, 3]

# Labs
# Adding student scores from a user and score and store them in a list. Then calculate the average score and print it.
# Then calculate the average score and print it.
scores = []
while True:
    score = input("Enter a student score (or type 'done' to finish): ")
    if score.lower() == 'done':
        break
    try:
        score = float(score)
        scores.append(score)
    except ValueError:
        print("Please enter a valid number.")

if scores:
    average = sum(scores) / len(scores)
    print(f"The average score is: {average}")
else:
    print("No valid scores were entered.")