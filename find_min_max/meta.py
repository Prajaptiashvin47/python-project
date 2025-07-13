import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 40]

# plt.plot(x, y, marker='o', linestyle='-', color='b', label="Growth")
# plt.xlabel("Time")
# plt.ylabel("Value")
# plt.title("Simple Line Graph")
# plt.legend()
# plt.show()
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # Step 1: Create a Sales Dataset using Pandas
# data = {
#     "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
#     "Sales": [1000, 1200, 1300, 900, 1500, 1700]
# }

# df = pd.DataFrame(data)  # Convert dictionary to DataFrame

# # Step 2: Calculate Sales Growth using NumPy
# df["Growth"] = np.diff([0] + df["Sales"].tolist())  # Compute growth from previous month

# # Step 3: Plot Sales Data using Matplotlib
# plt.figure(figsize=(8, 5))
# plt.plot(df["Month"], df["Sales"], marker="o", linestyle="-", color="b", label="Sales")
# plt.bar(df["Month"], df["Growth"], color="orange", alpha=0.6, label="Growth")

# plt.xlabel("Month")
# plt.ylabel("Sales & Growth")
# plt.title("Monthly Sales Analysis")
# plt.legend()
# plt.grid()
# plt.show()
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a line plot
plt.plot(x, y, marker='*', linestyle='-', color='b', label="Sales Growth")

# Add labels and title
plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Sales Growth Over Years")
plt.legend(loc="upper left", fontsize=15, title=" Data")

# Show the graph
plt.show()
