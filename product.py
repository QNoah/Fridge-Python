class Product:
    
    def __init__(self, name, total_qty):
        self.name = name
        self.total_qty = total_qty
    
    def add_product(self, qty):
        self.qty = qty
        print(f"Added: {self.name} with a quantity of {self.qty}")
        self.total_qty += self.qty
        print(f"New quantity: {self.total_qty}")
    
    def remove_product(self):
        if self.qty > 0:
            print(f"Removed: {self.name} with a quantity of {self.qty}")
        elif self.qty <= 0:
            print("Can't remove anymore products, because quantity is 0.")
        else:
            print("Your action could not be completed, try again later.")