num=int(input("enter the number"))
sum_digit = 0
while num > 0: 
    sum_digit += num %10
    num =num // 10
print("the total sum :",sum_digit)
    
     
 