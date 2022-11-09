class Item:
    def calculate_price(self, price: int, quantity: int) -> int: 
        # by default python pass object as the first parameter -> self
        return price * quantity


item1: object = Item()
item1.name: str = 'Phone'
item1.price: int = 500
item1.quantity: int = 5
print(item1.calculate_price(item1.price, item1.quantity))
print(type(item1), type(item1.name), type(item1.price))

item2: object = Item()
item2.name: str = 'Laptop'
item2.price: int = 1000
item2.quantity: int = 3
print(item1.calculate_price(item2.price, item2.quantity))