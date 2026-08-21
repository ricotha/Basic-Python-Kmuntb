def main():
    inventory = {}
    while True:
        print("1. Add a product")
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
                while True:
                    try:
                        price = float(input("Enter price: "))
                        if price >= 0:
                            break
                        print("Price must be >= 0. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                while True:
                    try:
                        quantity = int(input("Enter quantity: "))
                        if quantity >= 0:
                            break
                        print("Quantity must be >= 0. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                inventory[code] = {"name": name, "price": price, "quantity": quantity}
                print("Product added.")

        elif choice == "2":
            code = input("Enter product code: ")
            if code in inventory:
                print("  a. Stock in (add to quantity)")
                print("  b. Stock out (remove from quantity)")
                sub_choice = input("  Choose transaction type (a/b): ")

                if sub_choice == "a":
                    while True:
                        try:
                            amount = int(input("Enter quantity to stock in: "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    if amount < 0:
                        print("Stock-in amount cannot be negative.")
                    else:
                        inventory[code]["quantity"] += amount
                        print(f"Stocked in {amount}. New quantity: {inventory[code]['quantity']}")

                elif sub_choice == "b":
                    while True:
                        try:
                            amount = int(input("Enter quantity to stock out: "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    if amount < 0:
                        print("Stock-out amount cannot be negative.")
                    elif amount > inventory[code]["quantity"]:
                        print(f"Not enough stock. Current quantity: {inventory[code]['quantity']}")
                    else:
                        inventory[code]["quantity"] -= amount
                        print(f"Stocked out {amount}. New quantity: {inventory[code]['quantity']}")

                else:
                    print("Invalid transaction type.")
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
                print(f"Name: {product['name']}")
                print(f"Price: {product['price']}")
                print(f"Quantity: {product['quantity']}")
            else:
                print("Product not found.")

        elif choice == "5":
            if inventory:
                print("\n--- All Products ---")
                for code, product in inventory.items():
                    print(f"{code} - {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}")
            else:
                print("No products in inventory.")

        elif choice == "6":
            print("\n--- Low-Stock Products ---")
            found = False
            for code, product in inventory.items():
                if product["quantity"] < 5:
                    print(f"{code} - {product['name']} | Quantity: {product['quantity']}")
                    found = True
            if not found:
                print("No low-stock products.")

        elif choice == "7":
            print("\n--- Inventory Value ---")
            total = 0
            for code, product in inventory.items():
                value = product["price"] * product["quantity"]
                print(f"{code} - {product['name']} = {value}")
                total += value
            print(f"Total inventory value: {total}")

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()