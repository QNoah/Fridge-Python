import os
from products_list import Products_List
from product import Product

product_list = Products_List()

def add_product():
    product_name = input("Enter a name for your product: ")
    while True:
        try:
            product_qty = int(input("Enter the amount of quantity: "))
            break
        except ValueError:
            continue
    product = Product(product_name, product_qty)
    os.system("cls")
    product_list.add_product(product)
    
    while True:
        try:
            _ = input("Would you wish to enter another product? (Yes or No):").lower()
            if _ == "yes":
                add_product()
            elif _ == "no":
                menu()
            else:
                print("That is not a valid option")
                continue
        except ValueError:
            print("That is not a valid option")
            continue

def view_products():
    product_list.show_list()
    menu()


def menu():
    print("Menu:")
    print("1. Add product")
    print("2. Remove product")
    print("3. View List")
    while True:
        try:
            choice = int(input(""))
            os.system("cls")
            if choice == 1:
                add_product()
            elif choice == 2:
                print("keuze 2")
            elif choice == 3:
                view_products()
            else:
                print("That is not a valid option.")
                continue
        except ValueError:
            print("That is not a valid option.")
            continue


# product_1 = Product(1, "Egg", 2)
# # qty = int(input())
# product_list.add_product(product_1)

# print(product_list.show_list())

print("Welcome before we continue to visit your entire list of products, we first need to enter some products.")
add_product()