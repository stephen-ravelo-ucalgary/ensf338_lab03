import timeit
from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import sys

sys.setrecursionlimit(100000)

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)

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

if __name__ == "__main__":
    list_lengths = [1000, 2000, 4000, 8000, 16000, 32000]
    averages = []
    number = 1

    for list_length in list_lengths:
        arr = [x for x in range(list_length)]
        
        time = timeit.timeit(lambda: quicksort(arr, 0, list_length - 1), number = number)
        average = time / number
        averages.append(average)

        print("List length: %d\nAverage time taken: %f\n" % (list_length, average))

    ax = plt.figure().add_subplot()
    x_interp = np.linspace(np.min(list_lengths), np.max(list_lengths), 50)
    y_quadratic = interp1d(list_lengths, averages, kind="quadratic")
    ax.plot(x_interp, y_quadratic(x_interp), 'k', c='r', label="fitted curve")
    ax.scatter(list_lengths, averages, c='b', label="raw data")
    ax.set_title('Quick Sort')
    ax.set_ylabel('time')
    ax.set_xlabel('list Length')
    ax.set_ylim(0)
    ax.set_xlim(0)
    ax.legend()
    plt.show()