num = int(input("Enter a number: "))  # Example: 1234
reverse_num = 0

while num > 0:
    digit = num % 10  # Get last digit
    reverse_num = reverse_num * 10 + digit  # Add digit to reverse_num
    num = num // 10  # Remove last digit

print("Reversed Number:", reverse_num)
