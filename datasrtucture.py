stack = []  
stack.append("A")  # Push  
stack.append("B")  
stack.append("C")
stack.append("f")  

print(stack.pop())  # Output: f (Last element removed)
print(stack)
from collections import deque  

queue = deque(["G","A", "B", "C"])  
queue.append("D")
queue.append("F")# Add element  
print(queue.popleft())  # Output: A (First element removed)
print(queue)