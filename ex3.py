import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    comparison = 0
    swap = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if(arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swap += 1
            comparison += 1
    return comparison, swap

def genArr(size):
    return [random.randint(0, 100) for n in range(size)]

if __name__ == "__main__":
    sizes = list(range(10, 210, 10))
    comparisonsRes = []
    swapsRes = []
    
    for size in sizes:
        arr = genArr(size)
        comparison, swap = bubble_sort(arr.copy())
        comparisonsRes.append(comparison)
        swapsRes.append(swap)
