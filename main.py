import os
from products_list import Products_List
from product import Product

product_list = Products_List()

def add_product():
    print("Add Product:")
    print("Type menu to go to the menu")
    print("Enter a name for your product:")
    product_name = input("")
    if product_name == "menu":
        os.system("cls")
        menu()
    while True:
        try:
            product_qty = int(input("Enter the amount of quantity: "))
            break
        except ValueError:
            continue

    product = Product(name=product_name, total_qty=product_qty)
    os.system("cls")
    product_list.add_product(product)
    
    while True:
        try:
            _ = input("Would you wish to enter another product? (Y/N):").lower()
            if _ == "y":
                add_product()
                break
            elif _ == "n":
                menu()
                break
            else:
                print("That is not a valid option")
        except ValueError:
            print("That is not a valid option")


def add_qty():
    print("| Add QTY |")
    print("Type menu to go to the menu")
    print("-" * 40)
    product_list.show_list()
    print("-" * 40)
    while True:
        try:
            inp_id = input("Enter the id of the product: ")
            if inp_id == "menu":
                menu()
                break
            
        except ValueError:
            os.system("cls")
            print("That command does not exist")
            add_qty()


def view_products():
    product_list.show_list()
    menu()


def menu():
    print("| Menu |")
    print("-" * 40)
    print("1. Add product")
    print("2. Add Qty")
    print("3. Remove product")
    print("4. View List")
    while True:
        try:
            choice = int(input(""))
            os.system("cls")
            if choice == 1:
                add_product()
                break
            elif choice == 2:
                result = product_list.show_list()
                if result == "empty":
                    print("Not available, since there are no items in the list.")
                    menu()
                else:
                    add_qty()
                    break
            elif choice == 3:
                print("keuze 3")
                break
            elif choice == 4:
                view_products()
            else:
                print("That is not a valid option.")
                continue
        except ValueError:
            print("That is not a valid option.")
            continue


print("Welcome before we continue to visit your entire list of products, we first need to enter some products.")
add_product()