# num =[1,2,3,4,5]
# mul_num =list(filter(lambda x : x % 2 == 0,num))
# print(mul_num)

# squre = lambda x :x*x
# print(squre(5))

# nums =[1,2,3,4,5]
# ss =list(map(lambda x : x * x ,num))
# print(ss)
# from functools import reduce
# num11 =[1,2,3,4,5]
# sumall = reduce (lambda x,y : x + y,num)
# print(sumall)
# def decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# @decorator
# def greet():
#     print("Hello!")

# greet()
# print("hello".lower()) 
# L=['a', 'b', 'c', 'd']
# print("".join(L))
# print(type(type(int)))
# def show_info(d):
#     for key, value in d.items():
#         print(key, value)

# info = {"name": "Ashvin", "age": 21}
# show_info(info)
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# common = list(set(a) & set(b))
# not_common = list(set(a) ^ set(b))

# print("Common:", common)
# print("Non-common:", not_common)
arr = [5, 2, 9, 1]

for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)
