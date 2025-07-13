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
