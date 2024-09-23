import os
from products_list import Products_List
from product import Product

def menu():
    os.system("cls")
    print("Menu:")
    print("1. Add product")
    print("2. Remove product")
    print("3. View List")
    choice = int(input(""))
    try:
        if choice == 1:
            print("keuze 1")
    except ValueError:
        print("That is not a valid option.")
        menu()

product_list = Products_List()

# product_1 = Product(1, "Egg", 2)
# # qty = int(input())
# product_list.add_product(product_1)

# print(product_list.show_list())

print("Welcome before we continue to visit your entire list of products, we first need to enter some products.")
product_name = input("Enter a name for your product: ")
product_qty = int(input("Enter the amount of quantity: "))

menu()