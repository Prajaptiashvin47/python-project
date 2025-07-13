import pandas as pd

# Check Pandas version
print("Pandas Version:", pd.__version__)

# Create a simple DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 
        'Age': [25, 30, 35], 
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# Print DataFrame
print("\nSample DataFrame:")
print(df)
