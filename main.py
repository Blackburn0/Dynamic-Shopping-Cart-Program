def add_to_cart():
    cart = []  # List to store cart items
    while True:
        item_name = input("Enter item name (or 'done' to finish): ").strip()
        if item_name.lower() == "done":
            print("\n-- Cart Summary --")
            if not cart:
                print("Your cart is empty.")
            else:
                for item in cart:
                    print(f"Item: {item['name']}, Price: {item['price']}")
                total = sum(item['price'] for item in cart)
                print(f"Total Price: {total}")
            break
        try:
            price = float(input("Enter the price: ").strip())
            cart.append({"name": item_name, "price": price})
            print(f"Added to cart: {item_name} (Price: {price})\n")
        except ValueError:
            print("Invalid price. Please enter a valid number.")
