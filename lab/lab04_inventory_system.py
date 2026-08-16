inventory = {}

while True:
    print("\n1. Add a product")
    print("2. Update product quantity")
    print("3. Remove a product")
    print("4. Search for a product")
    print("5. Show all products")
    print("6. Show low-stock products")
    print("7. Calculate inventory value")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        code = input("Enter product code: ")
        if code in inventory:
            print("This product code already exists.")
        else:
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            inventory[code] = {"name": name, "price": price, "quantity": quantity}
            print("Product added.")

    elif choice == "2":
        code = input("Enter product code: ")
        if code in inventory:
            inventory[code]["quantity"] = int(input("Enter new quantity: "))
            print("Quantity updated.")
        else:
            print("Product not found.")

    elif choice == "3":
        code = input("Enter product code: ")
        if code in inventory:
            del inventory[code]
            print("Product removed.")
        else:
            print("Product not found.")

    elif choice == "4":
        code = input("Enter product code: ")
        if code in inventory:
            product = inventory[code]
            print("Name:", product["name"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])
        else:
            print("Product not found.")

    elif choice == "5":
        if inventory:
            for code, product in inventory.items():
                print(code, "-", product["name"], "| Price:", product["price"], "| Quantity:", product["quantity"])
        else:
            print("No products in inventory.")

    elif choice == "6":
        found = False
        for code, product in inventory.items():
            if product["quantity"] < 5:
                print(code, "-", product["name"], "| Quantity:", product["quantity"])
                found = True
        if not found:
            print("No low-stock products.")

    elif choice == "7":
        total = 0
        for code, product in inventory.items():
            value = product["price"] * product["quantity"]
            print(code, "-", product["name"], "=", value)
            total += value
        print("Total inventory value:", total)

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
