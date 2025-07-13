"""in this  swap the value without temp  """
x,y=5,10
print(x,y)
x,y=y,x
print(x,y)
"""for loop """
for i in range (1,6):
 print(i)
 """loop through list """
 fruits=["apple ","banana","cherry "]
for fruit in fruits:
        print(fruit)
"""while loop """
x=1
while x<=5:
    print(x)
    x+=1
    """gusse the game """
    """s_number=7
    gusse=0
    while gusse!=s_number:
        gusse=int(input("gusse number :"))
        print("you gusse right number ")
print(" youy gusse wrong number")      """ 
secret_number = 7  
guess = 0  

while guess != secret_number:  
    guess = int(input("Guess the number: "))  
    print("Wrong! Try again.")  

print("You guessed it right!")
"""loop control statment break and continue """
for i in range(1,6):
    if i==3:
        print(i)
