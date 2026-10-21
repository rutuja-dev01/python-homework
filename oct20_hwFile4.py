#class 04

class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

b1 = Building("Sunshine Tower", 10)
b2 = Building("Green Heights", 15)
b3 = Building("Sky Plaza", 5)
b4 = Building("Royal Residency", 20)
b5 = Building("City Center", 8)

building_list = []
building_list.append(b1)
building_list.append(b2)
building_list.append(b3)
building_list.append(b4)
building_list.append(b5)

for obj in building_list:
    if obj.name.startswith("S"):
        print(f"Building: {obj.name} --> Floors: {obj.floors}")
