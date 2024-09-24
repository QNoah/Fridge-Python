import random
import string

class Product:
    def __init__(self, name, total_qty, id=None):
        self.id = id if id else self.generate_id()
        self.name = name
        self.total_qty = total_qty
    
    
    def generate_id(self, length= 6):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    
    
    # reprr is nodig omdat het anders in binary gaat tonen
    def __repr__(self):
        return f"Id: {self.id}, Name: {self.name}, Qty: {self.total_qty}"
    
    
    def remove_product(self):
        pass


    def add_qty(self, qty):
        self.qty = qty
        print(f"Added: {self.name} with a quantity of {self.qty}")
        self.total_qty += self.qty
        print(f"New quantity: {self.total_qty}")


    # def remove_product(self):
    #     if self.qty > 0:
    #         print(f"Removed: {self.name} with a quantity of {self.qty}")
    #     elif self.qty <= 0:
    #         print("Can't remove anymore products, because quantity is 0.")
    #     else:
    #         print("Your action could not be completed, try again later.")