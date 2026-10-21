# Name: Nam Pham
# Period: AM
# Smart Shopping Cart

from datetime import date
today = date.today()

products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
prices = ["2.00", "2.50", "1.50", "3.00", "1.00", "5.00"]
# These two lists contain both the items and the prices of each item on the menu

shopping_cart = []
# This is where the products the customer adds will go

option = ""
total = 0

while option != "6":
    print("========== SMART SHOPPING CART ==========")
    print("")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")
    print("")
    option = input("Enter your choice: ")
# Here the customer chooses from 6 options for seperate purposes

    if option == "1":
        for product in products:
            print(product, "    ", "$", prices[products.index(product)])
    # This is to simply show the customer the whole menu when they select option 1

    elif option == "2":
        add_product = ""
        while add_product != "7":
            print("What product would you like to add?")
            print("")
            print("1. Chips")
            print("2. Soda")
            print("3. Candy")                
            print("4. Cookies")
            print("5. Water")
            print("6. Sandwich")
            print("7. Back to main menu")
            print("")
            add_product = input("Enter product number: ")
            if add_product == "1":
                shopping_cart.append("Chips")
                print("Chips have been added to your cart!")
            elif add_product == "2":
                shopping_cart.append("Soda")
                print("Soda has been added to your cart!")
            elif add_product == "3":
                shopping_cart.append("Candy")
                print("Candy has been added to your cart!")
            elif add_product == "4":
                shopping_cart.append("Cookies")
                print("Cookies have been added to your cart!")
            elif add_product == "5":
                shopping_cart.append("Water")
                print("Water has been added to your cart!")
            elif add_product == "6":
                shopping_cart.append("Sandwich")
                print("Sandwich has been added to your cart!")
            elif add_product == "7":
                print("Returning to main menu")
            else:
                print("Invalid product!")
                print("Please enter a valid number")
        for items in shopping_cart:
            cost = prices[products.index(items)]
            total += float(cost)
    # This much longer code allows the customer to add as many products to their cart as they want and adding to their total cost

    elif option == "3":
        print(">-----< Your Shopping Cart >-----<")
        print("")
        for product in shopping_cart:
            print(product)
        print("")
        if len(shopping_cart) == 0:
            print("Your cart is empty!")
            print("There's nothing to remove yet.")
        else: 
            print("Which item would you like to remove from your cart?")
            remove = input("Enter item number: ")
            while int(remove) > len(shopping_cart):
                print("Invalid option!")
                remove = input("Enter item number: ")
            shopping_cart.pop(int(remove) - 1)
    # This will be where the customer can remove any item in their cart, but will send them back to the main menu if their cart is empty

    elif option == "4":
        print(">-----< Your Shopping Cart >-----<")
        print("")
        if len(shopping_cart) == 0:
            print("Your cart is currently empty!")
        for items in shopping_cart:
            print(items, "    ", "$", prices[products.index(items)])
        print("")
        print("Total items: ", len(shopping_cart))
    # Here the customer can see the items and the prices of the items in their cart currently, but will send them back to the main menu if it's empty

    elif option == "5":
        total = 0
        print(">-----< Current Total >-----<")
        print("")
        for items in shopping_cart:
            print(items, "    ", "$", prices[products.index(items)])
        for items in shopping_cart:
            cost = prices[products.index(items)]
            total += float(cost)
        print("")
        print("Subtotal: ", "$", total)
    # Option 5 lets the customer see the current total, no discount yet, of their whole cart

    elif option == "6":
        print(">-----< Checkout >-----<")
        print("")
        if len(shopping_cart) == 0:
            print("Your cart is empty!")
            option = ""
        else:
            print(">-----< Receipt >-----<")
            print("")
            print(today)
            print("")
            print("Subtotal:", "$", total)
            if total < 10:
                discount = 0
            elif (total >= 10) and (total < 20):
                discount = 5
            elif (total >= 20) and (total < 40):
                discount = 10
            else:
                discount = 15
            print("Discount:", discount, "%")
            amount_saved = total * (int(discount)/100)
            print("Amount saved:", "$", amount_saved)
            print("")
            final_total = total - amount_saved
            print("Final total:", "$", final_total)
            print("")
            print("Thank for shopping here!")
            option = "6"
    # This is where the customer can checkout their items and the program will end, or it could send them back to the main menu if the cart is empty
    
    else:
        print("Invalid option")
    # Now this is to make sure that any other option choice of 1-6 will be deemed invalid