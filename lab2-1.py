#Wrrote a program to exchage currency from THB to ...
thb = float(input("Enter your money to exchange(฿): "))
country = input("Enter short country name:")
if country == "GBP":
    currenvy = thb * 45.2223
    print(f"Your money (thb) bath, exchange to {country} is: {currenvy}")
elif country == "AUD":
    currenvy = thb * 23.7270
    print(f"Your money (thb) bath, exchange to {country} is: {currenvy}")
elif country == "USA":
    currenvy = thb * 33.6516
    print(f"Your money (thb) bath, exchange to {country} is: {currenvy}")
elif country == "EURO":
    currenvy = thb * 38.6137
    print(f"Your money (thb) bath, exchange to {country} is: {currenvy}")
elif country == "JPY":
    currenvy = thb * 20.9627
    print(f"Your money (thb) bath, exchange to {country} is: {currenvy}")
else:
    print("Invalid country name. Please enter a valid country name (GBP, AUD, USA, EURO, JPY).")


"Your money (thb) bath, exchanfe to (country) is:(currenvy)"
"GBP"
"AUD"
"USA"
"EURO"
"JPY"