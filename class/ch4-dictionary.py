# # Dictionary- key-value pairs
# # my_dict = {}
# my_dict = {
#     'name': 'John',
#     'age': 30,
#     'city': 'New York',
#     'is_student': False
# }
# print(my_dict) # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'is_student': False}

# #Accessing values
# print(my_dict['name']) # Output: John
# print(my_dict['age']) # Output: 30
# print(my_dict['city']) # Output: New York
# print(my_dict['is_student']) # Output: False

# for key in my_dict:
#     print(key, my_dict[key]) # Output: name John age 30 city New York is_student False

# # Adding a new key-value pair
# my_dict['country'] = 'Thailand'
# print(my_dict) # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'is_student': False, 'country': 'Thailand'}

# # Updating a key-value pair
# my_dict["age"] = 45
# print(my_dict) # Output: {'name': 'John', 'age': 45, 'city': 'New York', 'is_student': False, 'country': 'Thailand'}

# # Removing a key-value pair
# del my_dict['is_student']
# print(my_dict) # Output: {'name': 'John', 'age': 45, 'city': 'New York', 'country': 'Thailand'}
# # or
# my_dict.pop('country')
# print(my_dict) # Output: {'name': 'John', 'age': 45, 'city': 'New York'}
# # or
# my_dict.clear()
# print(my_dict) # Output: {}

# # Nested dictionary
# my_dict = {
#     'name': 'John',
#     'age': 30,
#     'city': 'New York',
#     'is_student': False,
#     'country': 'Thailand',
#     'hobbies': {'reading': True, 'painting': False}
# }

# # Accessing nested dictionary values
# print(my_dict['hobbies']['reading']) # Output: True
# print(my_dict['hobbies']['painting']) # Output: False

# # Updating nested dictionary values
# my_dict['hobbies']['painting'] = True
# print(my_dict['hobbies']['painting']) # Output: True

# Labs 4.4 - Dictionary (5 mins)
# 1. Create a dictionary call 'inventory' with the following key-value pairs: 'apple' : 10, 'banana' : 5, 'orange' : 8.
# 2. Print the value of the 'apple' key.
# 3. Add a new key-value pair to the dictionary: 'grape' : 15.
# 4. Print the value of the 'grape' key.
# 5. Update the value of the 'banana' key to 10.
# 6. Print the updated dictionary.

invertory = {
    'apple': 10,
    'banana': 5,
    'orange': 8
}

print(invertory['apple']) # Output: 10
invertory['grape'] = 15
print(invertory['grape']) # Output: 15
invertory['banana'] = 10
print(invertory) # Output: {'apple': 10, 'banana': 10