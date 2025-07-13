def fin_min_max(tup):
    min_value=min(tup)
    max_value=max(tup)
    return min_value,max_value
num_tuple=(45,9,23,67,90)
min_val,max_val = fin_min_max(num_tuple)
print("tuple:",num_tuple)
print("Minimum Value:", min_val)
print("Maximum Value:", max_val)
        