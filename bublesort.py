def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  # Swap if needed
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [5, 3, 8, 2, 1]
bubble_sort(arr)
print("Sorted Array:", arr)
