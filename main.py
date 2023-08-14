import csv

class Products:
    all = []
    def __init__(self, name:str, price:float, quantity:int):
        self.name = name
        self.__price = price
        self.quantity = quantity

        # validations
        assert price >=0
        assert quantity >=0

        Products.all.append(self)

    def __repr__(self):
        return f"Products('{self.name}, {self.price}, {self.quantity}')"

    # Read products from the csv file
    @classmethod
    def show_csv(cls):
        with open('products.csv', 'r') as f:
            read = csv.DictReader(f)
            list_item = list(read)

        for item in list_item:
            Products(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),

            )

    # function to apply discount on prices 
    @property
    def set_discount(self, discount_value):
        self.__price = self.__price * discount_value

    # function to increase the price
    @property
    def increase_value(self, increament_value):
        self.__price = self.__price + increament_value
    


    

# Products.show_csv()
# print(Products.all)
