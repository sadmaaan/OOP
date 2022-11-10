import csv

class Item:
    pay_rate: float = 0.8
    all = [] # storing object in this

    def __init__(self, name: str, price: int, quantity=0) -> None:
        assert price >= 0, f"Price {price} is less than 0"
        assert quantity >= 0, f"Quantity {quantity} is less than 0"

        # assign self object
        self.__name = name # makes it private
        self.price = price
        self.quantity = quantity

        # stroring object
        Item.all.append(self)

    @property # makes name -> read only variable(JAVA -> private)
    def name(self):
        return self.__name

    @name.setter # setting value in private variable
    def name(self, new_value: str):
        if len(new_value) > 10:
            raise Exception("Name length should be lower!!!")
        else:
            self.__name = new_value
    
    # override __str()__ and __repr()__ to make our own object return type
    def __repr__(self):
        return f'Item("{self.name}", {self.price}, {self.quantity})'

    def calculate_price(self) -> int: 
        return self.price * self.quantity
    
    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate