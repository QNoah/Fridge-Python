from products_list import Products_List
from product import Product

product_list = Products_List()

product_1 = Product(1, "Egg", 2)
# qty = int(input())
product_list.add_product(product_1)

print(product_list.show_list())

# print("Welcome before we continue to visit your entire list of products, we first need to enter some products.")
