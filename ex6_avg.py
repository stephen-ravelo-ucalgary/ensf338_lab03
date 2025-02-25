import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = [10, 5]

def linear_search(key, arr):
    for i in range(len(arr)):
        if arr[i] == key:
            return True
    return False

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
        
def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
            
        while right >= left and arr[right] >= pivot:
            right -= 1
            
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
            
    arr[low], arr[right] = arr[right], arr[low]
    return right

def binary_search(arr, first, last, key):
    if first <= last:
        mid = (first + last) // 2 
        if key == arr[mid]:
            return True
        elif key < arr[mid]:
            return binary_search(arr, first, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, last, key)
    return False

def sortAndBinary(key, arr):
    arrCpy = arr.copy()
    quicksort(arrCpy, 0, len(arrCpy) - 1)
    return binary_search(arrCpy, 0, len(arrCpy) - 1, key)

if __name__ == "__main__":
    inputLength = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    linearSearchTimes = []
    sortAndBinaryTimes = []
    
    for n in inputLength:
        numbers = list(range(n))
        timesLinear = []
        timesSortBinary = []
        
        for x in range(100):
            random.shuffle(numbers)
            key = 5 if n > 5 else numbers[0]
            
            linearTime = timeit.timeit("linear_search(key, numbers)", setup="from __main__ import linear_search, numbers, key", number=100)
            linearTime /= 100
            timesLinear.append(linearTime)
            
            binaryTime = timeit.timeit("sortAndBinary(key, numbers)", setup="from __main__ import sortAndBinary, numbers, key", number=100)
            binaryTime /= 100
            timesSortBinary.append(binaryTime)
            
        avgLinear = sum(timesLinear) / len(timesLinear)
        avgBinary = sum(timesSortBinary) / len(timesSortBinary)
        linearSearchTimes.append(avgLinear)
        sortAndBinaryTimes.append(avgBinary)
    
    plt.scatter(inputLength, linearSearchTimes, label="Linear Search", color="b")
    plt.scatter(inputLength, sortAndBinaryTimes, label="Quicksort + Binary Search", color="r")
    
    linearSlope, linearInt = np.polyfit(inputLength, linearSearchTimes, 1)
    linearLine = [linearSlope * x + linearInt for x in inputLength]
    plt.plot(inputLength, linearLine, 'b--', label="Linear Regression (Linear Search)")
    
    binarySlope, binaryInt = np.polyfit(inputLength, sortAndBinaryTimes, 1)
    binaryLine = [binarySlope * x + binaryInt for x in inputLength]
    plt.plot(inputLength, binaryLine, 'r--', label="Linear Regression (Quicksort + Binary Search)")
    
    plt.xlabel("Input Size (n)")
    plt.ylabel("Average Time (seconds)")
    plt.title("Average-Case: Linear Search vs Quicksort + Binary Search")
    plt.legend()
    plt.show()
    
    print("The linear model is: t = %.2e * n + %.2e" % (linearSlope, linearInt))
    print("The quicksort + binary model is: t = %.2e * n + %.2e" % (binarySlope, binaryInt))


# Exercise 6 Part 4:
# From the plot, quicksort + binary search had a larger average time than the linear search.
# This is likely due to the data being sorted each time. With quicksort being O(nlog n) and binary search being O(log n), 
# quicksort + binary search is O(nlog n), while linear search is O(n). For the range of input sizes we used,
# n < nlog n, which explains why linear search is faster in this case. 