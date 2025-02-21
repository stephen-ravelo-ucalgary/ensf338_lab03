import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

# "Traditional" Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Binary Insertion Sort
def binary_search(arr, val, start, end):
	if start == end:
		if arr[start] > val:
			return start
		else:
			return start+1

	if start > end:
		return start

	mid = (start+end)//2
	if arr[mid] < val:
		return binary_search(arr, val, mid+1, end)
	elif arr[mid] > val:
		return binary_search(arr, val, start, mid-1)
	else:
		return mid

def binary_insertion_sort(arr):
	for i in range(1, len(arr)):
		val = arr[i]
		j = binary_search(arr, val, 0, i-1)
		arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
	return arr

# Insertion Sort average case: randomly ordered array
# Binary Insertion Sort average case: randomly ordered array

x_values = list(range(5, 105, 5))
ins_srt = []
bin_ins_srt = []

# Timing of the average case of both Insertion Sort and Binary Insertion Sort
for i in x_values:
    array = random.sample(range(i * 10), i)
	
    elapsed_time = timeit.timeit(lambda : insertion_sort(array.copy()), number = 1)
    ins_srt.append(elapsed_time)
	
    elapsed_time = timeit.timeit(lambda : binary_insertion_sort(array.copy()), number = 1)
    bin_ins_srt.append(elapsed_time)
    
# Plotting
x_values = np.array(x_values)
ins_srt = np.array(ins_srt)
bin_ins_srt = np.array(bin_ins_srt)

fit_ins = np.polyfit(x_values, ins_srt, deg = 2)
fit_bin_ins = np.polyfit(x_values, bin_ins_srt, deg = 2)

x_smooth = np.linspace(5, 100, 200)
y_ins_smooth = np.polyval(fit_ins, x_smooth)
y_bin_ins_smooth = np.polyval(fit_bin_ins, x_smooth)

plt.scatter(x_values, ins_srt, label = "Insertion Sort", marker = 'o', color = 'b')
plt.scatter(x_values, bin_ins_srt, label = "Binary Insertion Sort", marker = 'o', color = 'r')
plt.plot(x_smooth, y_ins_smooth, label = "Insertion Sort Interpolated", color ='b')
plt.plot(x_smooth, y_bin_ins_smooth, label = "Binary Insertion Sort Interpolated", color = 'r')

plt.title("Average Case")
plt.xlabel("Array Size (n)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

'''
Question 4 Answer
In the average case, the "traditional" insertion sort is faster than binary insertion sort.
Due to the nature of binary insertion sort, in order to sort the array it has to:
    - calculate the midpoint
    - compare the value at the midpoint
    - adjust search boundaries
On top of these operations, it still has to shift the elements to their proper place.
These additional operations can take up more time than how much is saved by reducing comparisons, like
in the average case of having a randomly ordered array. Unlike insertion sort where it just compares
the elements sequentially and then shifts these elements. Thus, in the average case, insertion sort
is faster than binary insertion sort.
'''
