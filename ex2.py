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

# Quick sort (modified to allow for case testing)
def quicksort(arr, low, high, pivot_type = "first"):
    if low < high:
        pivot_index = partition(arr, low, high, pivot_type)
        quicksort(arr, low, pivot_index - 1, pivot_type)
        quicksort(arr, pivot_index + 1, high, pivot_type)
    return arr

def partition(arr, low, high, pivot_type):
    if pivot_type == "random":
        pivot_index = random.randint(low, high)
    elif pivot_type == "middle":
        pivot_index = (low + high) // 2
    else:
        pivot_index = low
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

    pivot = arr[low]
    left = low + 1
    right = high
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

# Bubble sort cases:
# Worst - reversely sorted array
# Average - randomly ordered array
# Best - sorted array

# Quick sort cases:
# Worst - extremely unbalanced partitions, sorted array
# Average - randomly selected pivots, randomly ordered array
# Best - balanced partitions, sorted array

bb_srt_best = []
bb_srt_avg = []
bb_srt_worst = []
qk_srt_best = []
qk_srt_avg = []
qk_srt_worst = []

# input sizes
x_values = list(range(5, 105, 5))

# Timing of best and worst case of Quick sort, and best case of Bubble sort
for i in x_values:
    array = list(range(1, i + 1))   # sorted array

    elapsed_time = timeit.timeit(lambda: quicksort(array.copy(), 0, i - 1, "middle"), number=1)
    qk_srt_best.append(elapsed_time)

    elapsed_time = timeit.timeit(lambda: quicksort(array.copy(), 0, i - 1, "first"), number=1)
    qk_srt_worst.append(elapsed_time)

    elapsed_time = timeit.timeit(lambda: bubble_sort(array.copy()), number=1)
    bb_srt_best.append(elapsed_time)

# Timing of average case of both Quick sort and Bubble sort
for i in x_values:
    array = random.sample(range(i * 10), i)    # randomly ordered array

    elapsed_time = timeit.timeit(lambda: quicksort(array.copy(), 0, i - 1, "random"), number=1)
    qk_srt_avg.append(elapsed_time)

    elapsed_time = timeit.timeit(lambda: bubble_sort(array.copy()), number=1)
    bb_srt_avg.append(elapsed_time)

# Timing of worst case of Bubble sort
for i in x_values:
    array = list(range(i, 0, -1))   # reversely sorted array

    elapsed_time = timeit.timeit(lambda: bubble_sort(array.copy()), number=1)
    bb_srt_worst.append(elapsed_time)


# Performance Plots
fig, axes = plt.subplots(3, 1, figsize = (8, 12))

titles = ["Best Case", "Worst Case", "Average Case"]
data_quick = [qk_srt_best, qk_srt_worst, qk_srt_avg]
data_bubble = [bb_srt_best, bb_srt_worst, bb_srt_avg]

for i, ax in enumerate(axes):
    ax.plot(x_values, data_quick[i], label = "Quick Sort", marker = "o", linestyle = "-", color = "b")
    ax.plot(x_values, data_bubble[i], label = "Bubble Sort", marker = "s", linestyle = "--", color = "r")
    ax.set_title(titles[i])
    ax.set_xlabel("Array Size (n)")
    ax.set_ylabel("Time (seconds)")
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.show()
