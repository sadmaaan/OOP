class Item:
    pay_rate: float = 0.8

    def __init__(self, name: str, price: int, quantity=0) -> None:
        assert price >= 0, f"Price {price} is less than 0"
        assert quantity >= 0, f"Quantity {quantity} is less than 0"

        self.name = name
        self.price = price
        self.quantity = quantity
   
    def calculate_price(self) -> int: 
        return self.price * self.quantity
    
    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate

if __name__ == "__main__":
    item1 = Item('Phone', 500, 5)
    item1.apply_discount()
    print(item1.price) # dont have its own discount rate so accessing the class level variable which belongs to class -> Item

    item2 = Item('Laptop', 1000, 3)
    item2.pay_rate: float = 0.7
    item2.apply_discount()
    print(item2.price) # it has its own discount rate so apllying its own discount rate
