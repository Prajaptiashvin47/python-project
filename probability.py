import random
import numpy as np
# Simulate rolling a dice 1000 times
trials = 1000
success = 0

for _ in range(trials):
    roll = random.randint(1, 6)  # Dice roll (1 to 6)
    if roll == 6:
        success += 1

# Calculate Probability
probability = success / trials
print(f"Probability of rolling a 6: {probability:.2f}")

arr=np.array([1,2,3,4,5],dtype=float)
print(arr)
print(type(arr))

matrix=np.array([[1,2,3],[4,5,6]])
print(matrix)
print(np.zeros((3, 3)))