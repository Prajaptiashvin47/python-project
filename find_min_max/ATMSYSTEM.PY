balance = 1000
def show_menu() :
    print(" ATM MENU ")
    print("1.check balance ")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")
    
def check_balance() :
       print(f"\n your current balance {balance} : ")
def deposit_money(amount) :
       global balance
       balance += amount
       print(f"/n{amount}")
def withdraw_money(amount) :
       global balance
       if  amount > balance :
        print("sufficient balance")  
       else :
         balance -= amount
         print(f"{amount}succefully withdraw to your account ")
while True:        
      show_menu()        
      choice = input("choice option ")
      if choice == '1' :
          check_balance()
      elif choice == '2' :
          amt = float(input("enter deposit money"))    
          deposit_money(amt)
      elif choice == '3' :
          amt = float(input("enter withdraw money"))    
          withdraw_money(amt)    
      elif choice == '4' :
          print("\n thank... you welcome back ")
          break 
      else :
          print("invalid choice ")
          