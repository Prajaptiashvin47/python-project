# count = 0
# def increase ():
#     global count 
#     count += 1
#     increase ()
#     print ()
    
def get_aversge(number):
       return sum(number) / len(number)
data = [10,20,30,40]
print(get_aversge(data))