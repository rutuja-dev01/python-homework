
# Single Inheritance = One parent, One child

class Parent :
    def parent_method(self) :
        print("This is a Parent method..")

class Child(Parent) :
    def child_method(self) :
        print("This is a Child method..")

obj = Child()
obj.parent_method()
obj.child_method()

obj2 = Parent()
obj2.parent_method()
obj2.child_method()                 # error 



# Multi-level Inheritance = One grandparent, One parent, One child

class Grandparent() :
    def grandparent_method(self) :
        print("This is a Grandparent method..")

class Parent(Grandparent) :
    def parent_method(self) :
        print("This is a Parent method..")

class Child(Parent) :
    def child_method(self) :
        print("This is a Child method..")

obj1 = Grandparent()
obj1.grandparent_method()
obj1.parent_method()                # error 
obj1.child_method()                 # error

obj2 = Parent()
obj2.grandparent_method()
obj2.parent_method()
obj2.child_method()                   # error 

obj3 = Child()
obj3.grandparent_method()
obj3.parent_method()
obj3.child_method()



# Hierachical Inheritance = One parent, Many children

class Parent :
    def parent_method(self) :
        print("This is a Parent method..")

class Child_1(Parent) :
    def child1_method(self) :
        print("This is First born child..")

class Child_2(Parent) :
    def child2_method(self) :
        print("This is Second born child..")

class Child_3(Parent) :
    def child3_method(self) :
        print("This is Last born child..")

obj1 = Parent()
obj1.parent_method()
obj1.child1_method()                    # error
obj1.child2_method()                    # error
obj1.child3_method()                    # error

obj2 = Child_1()
obj2.parent_method()
obj2.child1_method()
obj2.child2_method()                    # error
obj2.child3_method()                    # error

obj3 = Child_2()
obj3.parent_method()
obj3.child2_method() 
obj3.child1_method()                    # error
obj3.child3_method()                    # error

obj4 = Child_3()
obj4.parent_method()
obj4.child3_method()
obj4.child1_method()                    # error
obj4.child2_method()                    # error



# Multiple Inheritance = Multiple parents, One child

class Parent_1_Mom :
    def parent1_method(self) :
        print("This is Mom..")

class Parent_2_Dad : 
    def parent2_method(self) :
        print("This is Dad..")

class Child(Parent_1_Mom, Parent_2_Dad) :
    def child_method(self) :
        print("This is child..")

obj1 = Parent_1_Mom()
obj1.parent1_method()
obj1.parent2_method()                   # error
obj1.child_method()                     # error

obj2 = Parent_2_Dad()
obj2.parent2_method()
obj2.parent1_method()                   # error
obj2.child_method()                     # error

obj3 = Child()
obj3.parent1_method()
obj3.parent2_method()
obj3.child_method()



# Hybrid Inheritance = Combo of diff. inheritance

# Parent class
class Grandparent:
    def show_grandparent(self):
        print("I am Grandparent")


# Multilevel inheritance
class Parent(Grandparent):
    def show_parent(self):
        print("I am Parent")


# Multiple inheritance
class Mother:
    def show_mother(self):
        print("I am Mother")


class Child(Parent, Mother):
    def show_child(self):
        print("I am Child")


# Creating object
c = Child()

c.show_grandparent()
c.show_parent()
c.show_mother()
c.show_child()
