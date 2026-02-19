import sys
from time import sleep
from users import UserManager
from products import ProductManager
from cart_and_orders import ShoppingCart, OrderManager

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()

def main():
    user_system= UserManager()
    catalog= ProductManager()
    order_history= OrderManager()
    
    current_user= None

    slow_print("--- Welcome to the Star Shopping ---")

    while True:
        if not current_user:
            print("\n1. Login")
            print("2. Register")
            print("3. Exit")
            
            choice= input("\nWhat would you like to do? ").strip()

            if choice== "1" or choice.lower()== "login":
                un= input("Username: ")
                pw= input("Password: ")
                success, result= user_system.login(un, pw)
                if success:
                    current_user= result
                    slow_print(f"\nHello {current_user['username']}! Logging you in...")
                else:
                    print(result)

            elif choice== "2" or choice.lower()== "register":
                un= input("Choose a username: ")
                pw= input("Choose a password (min 6 chars): ")
                success, msg= user_system.register(un, pw)
                print(msg)

            elif choice== "3" or choice.lower()== "exit":
                slow_print("Closing Star Shopping. We look forward to seeing you again!")
                sys.exit()

        else:
            my_cart= ShoppingCart() 
            
            while current_user:
                print(f"\n--- STORE MENU (User: {current_user['username']}) ---")
                print("1. Browse All Products")
                print("2. Search for a Product")
                print("3. View Shopping Bag")
                print("4. Add Item to Bag")
                print("5. View Order History")
                print("6. Checkout")
                print("7. Logout")

                task= input("\nSelect an option(numerical): ").strip()

                if task== "1":
                    products= catalog.list_products()
                    print(f"\n{'ID':<10} {'Name':<30} {'Price':<10} {'Stock':<10}")
                    print("-"*60)
                    for p in products:
                        print(f"{p['product_id']:<10} {p['name']:<30} ${p['price']:<9.2f} {p['stock']:<10}")

                elif task== "2":
                    query= input("Enter keyword to search: ")
                    results= catalog.search_products(query)
                    if results:
                        for p in results:
                            print(f"-> {p['name']} (${p['price']}) - ID: {p['product_id']} [Stock: {p['stock']}]")
                    else:
                        print("No products found matching that name.")

                elif task== "3":
                    my_cart.show_bag_contents()

                elif task== "4":
                    p_id= input("Enter the Product ID: ")
                    item= catalog.get_product(p_id)
                    if item:
                        try:
                            qty= int(input(f"How many {item['name']}? "))
                            if item['stock'] >=qty:
                                my_cart.add_to_bag(item, qty)
                            else:
                                print(f"Sorry, we only have {item['stock']} in stock.")
                        except ValueError:
                            print("Please enter a valid number for quantity.")
                    else:
                        print("Invalid Product ID.")

                elif task== "5":
                    orders= order_history.get_orders_for_user(current_user['username'])
                    if not orders:
                        print("No orders yet.")
                    else:
                        print("\n--- Your Past Orders ---\n")
                        for o in orders:
                            print(f"Order ID: {o['order_id']}")
                            print(f"Date: {o['timestamp']}")
                            print(f"Total: ${o['total']:.2f}")
                            print("Items:")
                            for item in o['items']:
                                print(f"  - {item['name']} x{item['qty']} - ${item['unit_price']:.2f} each")
                            print("-"* 40)

                elif task== "6":
                    if not my_cart.contents:
                        print("Your bag is empty! Add something before checking out.")
                    else:
                        my_cart.show_bag_contents()
                        confirm= input("Confirm purchase? (y/n): ").lower()
                        if confirm== "y":
                            order_id= order_history.record_new_order(
                                current_user["username"], 
                                my_cart.contents, 
                                my_cart.calculate_total()
                            )
                            
                            for item in my_cart.contents:
                                catalog.update_stock(item["product_id"], -item["qty"])
                            
                            my_cart.empty_bag()
                            print(f"Success! {order_id} placed.")

                elif task== "7":
                    current_user= None
                    print("Logged out successfully.")

if __name__=="__main__":
    main()