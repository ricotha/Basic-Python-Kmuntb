#Loops flow comtrol
#While loops
# i = 0
# while (i < 5):
#     print(i)
#     i +=1           #i = i+1

# #For loop
# for i in range(5):
#     print(i)

# for i in range( 1, 5, 1): #start, stop, step
#     print(i)

# for i in range( 1, 10, 2): #start, stop, step
#     print(i)

# for i in range(10):
#     print(i)

#Example 1 
# number = int(input("Enter a number: "))
# for i in range(1, number + 1):
#     print(i)

# #Nested loop
# for i in range(1, 5):
#     for j in range(1, 5):
#         print(i, "," ,j)

# #Special keywerds: break, continue, pass
# answer = 20
# rand_answer = 0 
# while True:
#     if(answer == rand_answer):
#         print("You win")
#         break
#     print(rand_answer)
#     rand_answer +=1

#Exercise 3.1
#Input a word
#if you input "exit" or EXIT
#The program will stop and print words you input

# word = input("Enter a word: ")
# while True:
#     if word.lower() == "exit":
#         print("Program stopped")
#         break
#     print(word)
#     word = input("Enter a word: ")


#Exercise lab 3.2 - Guess the number
# import random
# rand_number = random.randint(1, 100)

# while True:
#     guess_number = int(input("Guess a number: "))
#     if guess_number == rand_number:
#         print("You win")
#         break
#     elif guess_number < rand_number:
#         print("Too small try again")
#     else:
#         print("Too big, try again")


# Exercise lab 3.3 - ATM Withdrawal
# Req.
# Set the account balance to 1M
# Set the withdraw limit to 50K per transaction
# Asked the user PIN : 1234
# Ask the user how much to withdraw

# If the user enters a number greater tha the withdrawal  limit, 
# print "Exceed the withdrawal limit"
# If the user enters a number greater than the account balance,
# print "Insufficient balance"

# Display the remaining balance

# Save as student_name_lab3-3.py
# Result
# Enter PIN: 1234
# Enter amount to withdraw: 100000
# Exceed withdrawal limit <---- Repeat this step until the user enters a valid amount

# Enter PIN: 1234
# Enter amount to withdraw: 50000
# Withdrawal successful
# Remaining balance: 950000
# Do you want to withdraw more? (y/n): 

account_balance = 1000000
withdraw_limit = 50000
pin = input("Enter PIN: ")
if pin == "1234":
    withdraw_amount = int(input("Enter amount to withdraw: "))
    if withdraw_amount > withdraw_limit:
        print("Exceed withdrawal limit")
    elif withdraw_amount > account_balance:
        print("Insufficient balance")
    else:
        account_balance -= withdraw_amount
        print("Withdrawal successful")
        print(f"Remaining balance: {account_balance}")