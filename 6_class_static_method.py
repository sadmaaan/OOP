import csv

class Item:
    pay_rate: float = 0.8
    all = [] # storing object in this

    def __init__(self, name: str, price: int, quantity=0) -> None:
        assert price >= 0, f"Price {price} is less than 0"
        assert quantity >= 0, f"Quantity {quantity} is less than 0"

        # assign self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # stroring object
        Item.all.append(self)
    
    # override __str()__ and __repr()__ to make our own object return type
    def __repr__(self):
        return f'Item("{self.name}", {self.price}, {self.quantity})'
    
    @classmethod
    def instantiate_from_csv(cls) -> None:
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
            
    @staticmethod
    def is_integer(num) -> bool:
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def calculate_price(self) -> int: 
        return self.price * self.quantity
    
    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate

if __name__ == "__main__":

    Item.instantiate_from_csv()
    print(Item.is_integer(4))
