#class 03

class Hospital:
    def __init__(self, name, beds):
        self.name = name
        self.beds = beds

h1 = Hospital("City Hospital", 100)
h2 = Hospital("Life Care", 80)
h3 = Hospital("Ruby Hospital", 150)
h4 = Hospital("Hope Hospital", 60)
h5 = Hospital("Sunrise Hospital", 120)

hospital_list = []
hospital_list.append(h1)
hospital_list.append(h2)
hospital_list.append(h3)
hospital_list.append(h4)
hospital_list.append(h5)

for obj in hospital_list:
    if obj.beds > 100:
        print(f"Hospital: {obj.name} --> Beds: {obj.beds}")
