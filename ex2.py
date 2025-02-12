import random
import timeit
import matplotlib.pyplot as plt

# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

# Quick sort
def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

# Bubble sort cases:
# Worst - reversely sorted
# Average - randomly ordered
# Best - sorted

# Quick sort cases:
# Worst - extremely unbalanced partitions
# Average - randomly selected pivots
# Best - balanced partitions

# 20 different input sizes
# each must be tested for worst, average, and best

# random array
array = random.sample(range(100), 10)
print(array)
# sorted array
print(list(range(1, 11)))
# reversely sorted array
print(list(range(10, 0, -1)))

# increment size of input by 20
x = 0
for i in range(5, 105, 5):
    print(i)
    x += 1
print(x)

x_values = list(range(5, 105, 5))
print(x_values)
print(len(x_values))