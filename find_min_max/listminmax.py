def fin_min_max(lst):
    min_value=min(lst)
    max_value=max(lst)
    return min_value,max_value
num_list=[45,9,23,67,90]
min_val,max_val = fin_min_max(num_list)
print("List:", num_list)
print("Minimum Value:", min_val)
print("Maximum Value:", max_val)
        