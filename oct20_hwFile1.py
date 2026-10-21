#class 01

class Zudio:
    def __init__(self,item,price):
        self.item = item
        self.price = price 

z1 =  Zudio("Shirt", 599)
z2 = Zudio("T-shirt", 299)
z3 = Zudio("Jeans", 899)
z4 = Zudio("Dress", 799)
z5 = Zudio("Top", 399)

zudio_list = []
zudio_list.append(z1)
zudio_list.append(z2)
zudio_list.append(z3)
zudio_list.append(z4)
zudio_list.append(z5)

for obj in zudio_list:
    if obj.price > 500:
        print(f"Item: {obj.item} --> Price: {obj.price}")
