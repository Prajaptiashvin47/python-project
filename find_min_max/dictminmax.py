# Function to find min and max values along with names in a dictionary
def find_min_max_dict(dct):
    # Finding the minimum and maximum values
    min_value = min(dct.values())
    max_value = max(dct.values())

    # Finding the names associated with the min and max values
    min_name = [key for key, value in dct.items() if value == min_value]
    max_name = [key for key, value in dct.items() if value == max_value]

    return min_name, min_value, max_name, max_value

# Example Dictionary (Names as Keys, Scores as Values)
score_dict = {
    "Alice": 87,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 89,
    "Frank": 78,  # Same min value as Charlie
    "Grace": 95   # Same max value as David
}

# Calling Function
min_names, min_val, max_names, max_val = find_min_max_dict(score_dict)

# Display Output
print("Dictionary:", score_dict)
print("Minimum Value:", min_val, "by", ", ".join(min_names))
print("Maximum Value:", max_val, "by", ", ".join(max_names))
