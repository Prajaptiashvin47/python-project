nums=[1,2,3,4,5]
squred=list(map(lambda x : x**2,nums))
print("using lamda funcation ",squred)
# 10% tax on all prices using lamada funcation 
price =[100,200,321,435]
final_price = list(map(lambda p : p + (p *0.10),price))
print("after tax add ",final_price)
#explicit conversation 
a = "123"
y =int(a)
print(y)
z=float(y)
print(z)

#string funcation 
a ="ashvin"
print(a.upper())
d="jay GOGA "
print(d.lower())
j="python is easy "
print(j.replace("python","coding"))

#logical opretor 
a=5
b=10
print(a < 10 and b < 15)

a=5
b=10
print(a < 2 or b < 2)