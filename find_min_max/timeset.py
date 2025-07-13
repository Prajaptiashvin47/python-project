# import time 
# start = time.time()
# for i in range (1000):
#     pass
# end = time.time()
# print(end - start)
# import requests
# response =requests.get("www.google.com")
# print("responense status",response.status_code)
# print("content",response.text[:100])
# class Grandparent:
#     def show(self):
#         print("Grandparent")

# class Parent(Grandparent):
#     def display(self):
#         print("Parent")

# class Child(Parent):
#     def hello(self):
#         print("Child")

# c = Child()
# c.show()
# c.display()
# c.hello()
# class Father:
#     def skills(self):
#         print("Gardening")

# class Mother:
#     def skills(self):
#         print("Cooking")

# class Child(Father, Mother):
#     def skills(self):
#         print("I have many skills!")

# c = Child()
#c.skills()
# class Parent:
#     def show(self):
#         print("Parent class")

# class Child1(Parent):
#     def child1_func(self):
#         print("Child1 class")

# class Child2(Parent):
#     def child2_func(self):
#         print("Child2 class")

# c1 = Child1()
# c2 = Child2()
# c1.show()
# c2.show()
class A:
    def show(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C:
    def showC(self):
        print("Class C")

class D(B, C):
    def showD(self):
        print("Class D")

d = D()
d.show()
d.showB()
d.showC()
d.showD()
