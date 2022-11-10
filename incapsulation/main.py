from item import Item

item1 = Item("RandomValue", 10000, 50)
# item1.apply_discount()
# print(item1.price)
print(item1.name)

# 1
# item1._name = "TempName" # still accessable
# print(item1.name)

# 2
# item1.__name = "TempName" # can't accessable -> name becames private and restricted to only Item class
# print(item1.name)

# 3
item1.name = "TempName" # making accessable in Item -> using setter
print(item1.name)