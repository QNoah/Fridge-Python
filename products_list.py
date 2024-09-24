class Products_List:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.product = product
        self.products.append(product)
        print(f'"{self.product.name}" added to the list')
    
    def show_list(self):
        if self.products != []:
            for product in self.products:
                print(product)
        else:
            print("Your list is empty")
            return "empty"