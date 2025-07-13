import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}
df = pd.DataFrame(data)
df["Salary"] = df["Salary"].astype(float) 
df.to_csv("Name.csv", index=False)
df = pd.read_csv("Name.csv") 
print(df)
