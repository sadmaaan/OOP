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
   
    def calculate_price(self) -> int: 
        return self.price * self.quantity
    
    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate

if __name__ == "__main__":
    item1 = Item('Phone', 500, 5)
    item2 = Item('Laptop', 1000, 3)
    item3 = Item('Tablet', 600, 2)
    item4 = Item('AC', 998, 1)
    item5 = Item('Fridge', 800, 9)
    item6 = Item('TV', 10000, 4)

    print(Item.all) # it has all the 6 objects

    # print specific attribute of objects
    for object in Item.all:
        print(f"{object.name} : {object.price}$")