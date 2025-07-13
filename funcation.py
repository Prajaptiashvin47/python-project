def greet():  
    print("Hello, Welcome to Python!")  

greet()  # Calling the function
"""calling funcation parameters """
def greet(name):
  print("hello",name)
greet("alice")
greet("john")
"""retutn keyword"""
def add(x,y):
    return x+y
result= add(5,3)
print(result)




add = lambda x,y : x+y
print(add(4,6)) #out put 10 