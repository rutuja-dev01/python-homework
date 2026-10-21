#class 05

class Library:
    def __init__(self, book, pages):
        self.book = book
        self.pages = pages

l1 = Library("Python", 250)
l2 = Library("Java", 450)
l3 = Library("SQL", 180)
l4 = Library("C++", 350)
l5 = Library("HTML", 150)

library_list = []
library_list.append(l1)
library_list.append(l2)
library_list.append(l3)
library_list.append(l4)
library_list.append(l5)

for obj in library_list:
    if obj.pages == 250:
        print(f"Book: {obj.book} --> Pages: {obj.pages}")