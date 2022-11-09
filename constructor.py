class Item:
    pay_rate: float = 0.8 # pay rate after 20% discount

    def __init__(self, name: str, price: int, quantity=0) -> None: # assert -> price shouldn't be less than 0
        assert price >= 0, f"Price {price} is less than 0"
        assert quantity >= 0, f"Quantity {quantity} is less than 0"

        # constructor variable declaration
        self.name = name
        self.price = price
        self.quantity = quantity

    # method    
    def calculate_price(self) -> int: 
        return self.price * self.quantity


item1: object = Item('Phone', 500, 5)
# print(item1.calculate_price())
item2: object = Item('Laptop', 1000, 3)
# print(item2.calculate_price())

# accessing class attribute
print(Item.pay_rate)
print(item1.pay_rate) # it first search in item1 instance if didn't find then search in class attibutes if find then print it
print(item2.pay_rate)

# checking which variables belongs to which objects
print(Item.__dict__)
print(item1.__dict__)
print(item2.__dict__)