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
    
    # override __repr()__ to make our own object return type
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.price}, {self.quantity})'

    def calculate_price(self) -> int: 
        return self.price * self.quantity
    
    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate

class Phone(Item):
    def __init__(self, name: str, price: int, quantity=0, broken=0) -> None:
        super().__init__(
            name, price, quantity
        )

        assert broken >=0, "{broken} should be greater than 0"
        self.broken = broken
        

if __name__ == '__main__':
    phone1 = Phone("Phone1", 550, 5, 1)
    # phone1.broken = 1
    print(phone1.calculate_price())
    phone1.apply_discount() # parent discount -> 20%
    print(phone1.price)

    # print -> created object belongs to which class
    print(Item.all)
    print(Phone.all)