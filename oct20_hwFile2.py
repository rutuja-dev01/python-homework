#class 02

class Restaurant:
    def __init__(self, name, price):
        self.name = name
        self.price = price

r1 = Restaurant("Pizza Hut", 250)
r2 = Restaurant("Dominos", 400)
r3 = Restaurant("Burger King", 180)
r4 = Restaurant("Cafe Coffee Day", 300)
r5 = Restaurant("McDonalds", 220)

restaurant_list = []
restaurant_list.append(r1)
restaurant_list.append(r2)
restaurant_list.append(r3)
restaurant_list.append(r4)
restaurant_list.append(r5)

for obj in restaurant_list:
    if obj.price > 250:
        print(f"Expensive: {obj.name} --> Price: {obj.price}")
    else:
        print(f"Affordable: {obj.name} --> Price: {obj.price}")
