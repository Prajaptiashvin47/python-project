"""creat class And object """

"""class car :
 def _init_(self,brand,color):
    self.brand=brand
    self.color=color
    def show_details(self):
        print(f"car brand: {self.brand},color:{self.color}")
        car1 =car("farari","red")
        car2 =car("BMW","black")
        car1.show_details()
        car2.show_details()"""
"""class Car:  
    def __init__(self, brand, color):  
        self.brand = brand  
        self.color = color  

    def show_details(self):  
        print(f"Car Brand: {self.brand}, Color: {self.color}")  

# Creating objects  
car1 = Car("Ferrari", "Red")  
car2 = Car("BMW", "Blue")  

car1.show_details()  # Output: Car Brand: Ferrari, Color: Red  
car2.show_details()  # Output: Car Brand: BMW, Color: Blue
"""


"""encapsulation """ 
"""class bankaccount:
 def _init(self,balance):
     self._balance=balance
def get_balance(self):
    return self._balance
def deposite(self,account):
    self._balance += amount
account=bankaccount(1000)
print(account.get_balance())
account.deposite(5000)
print(account.get_balance)"""
class BankAccount:  
    def __init__(self, balance):  
        self.__balance = balance  # Private variable  

    def get_balance(self):  
        return self.__balance  

    def deposit(self, amount):  
        self.__balance += amount  

# Creating an account  
account = BankAccount(1000)  
print(account.get_balance())  # Output: 1000  

account.deposit(500)  
print(account.get_balance())  # Output: 1500  

# print(account.__balance)  # ❌ This will cause an error (private variable)
""" inheritance """
class animal:
 def sound(self):
     print("aniaml sound")
class dog(animal):
    def sound(self):
        print("dog bark ")
        
        
        dog = dog()
        dog.sound()
        
class Animal:  
    def sound(self):  
        print("Animals make sound")  

class Dog(Animal):  # Dog inherits from Animal  
    def sound(self):  
        print("Dog barks")  

dog = Dog()  
dog.sound()  # Output: Dog barks
