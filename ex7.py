import json
import timeit
from matplotlib import pyplot as plt
import sys
import pandas as pd
import numpy as np

sys.setrecursionlimit(20000)

def binary_search(arr, first, last, key, mid, count):
    if (first <= last):
        if (count != 0):
            mid = (first + last) // 2
        count += 1
        if (key == arr[mid]):
            return mid
        elif (key < arr[mid]):
            return binary_search(arr, first, mid - 1, key, mid, count)
        else:
            return binary_search(arr, mid + 1, last, key, mid, count)
    return -1

if __name__ == '__main__':
    # Load files
    files_loaded = False
    try:
        with open('ex7data.json', mode='r', encoding='utf-8') as data_file:
            file_contents = data_file.read()
        data = json.loads(file_contents)
        with open('ex7tasks.json', mode='r', encoding='utf-8') as tasks_file:
            file_contents = tasks_file.read()
        tasks = json.loads(file_contents)
        files_loaded = True
    except:
        print('Data unsuccessfully loaded.')
        quit(1)
    
    # Estimate best midpoint for each task
    precision = 5000
    midpoints = [precision * x for x in range(len(data) // precision)]
    best_midpoints = []
    number = 100
    for task in tasks:
        averages = []
        for midpoint in midpoints:
            time = timeit.timeit(lambda: binary_search(data, 0, len(data) - 1, task, midpoint, 0), number = number)
            average = time / number
            averages.append(average)
        
        best_time = min(averages)
        best_midpoint = midpoints[averages.index(best_time)]
        best_midpoints.append(best_midpoint)
        best_time_ms = best_time * 1000
        df_data = np.array([[int(task), best_midpoint, best_time_ms]])
        df = pd.DataFrame(df_data, columns=['key', 'best initial midpoint', 'average time'])
        df['key'] = np.int64(df['key'])
        df['best initial midpoint'] = np.int64(df['best initial midpoint'])
        print(df.to_string(index=False))

    # Plot graph
    ax = plt.figure().add_subplot()
    ax.scatter(tasks, best_midpoints)
    ax.set_title('key vs. best initial midpoint')
    ax.set_xlabel('best initial midpoint')
    ax.set_ylabel('key')
    ax.set_ylim(0)
    ax.set_xlim(0)
    plt.show()
    
    '''
    Question 4
    Based on the graph the best initial midpoint is on average the point
    closest to the key. The reason for this is likely because it is the
    point that is able to create the smallest possible sub-array to then
    continue on with regular binary search.
    '''

    # Close files
    if (files_loaded):
        data_file.close()
        tasks_file.close()