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
balance = 1000000
limit = 50000
pin = "1234"

if input("Enter PIN: ") == pin:
    more = "y"
    while more == "y":
        while True:
            amt = int(input("Enter amount to withdraw: "))
            if amt > limit:
                print("Exceed withdrawal limit")
            elif amt > balance:
                print("Insufficient balance")
            else:
                break
        balance -= amt
        print("Withdrawal successful")
        print("Remaining balance:", balance)
        more = input("Do you want to withdraw more? (y/n): ")
else:
    print("Incorrect PIN")