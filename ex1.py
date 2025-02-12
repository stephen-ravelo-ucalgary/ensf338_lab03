def merge(arr, low, mid, high):
    l_length = mid - low + 1
    r_length = high - mid

    left_arr = [0] * l_length
    right_arr = [0] * r_length

    for i in range(l_length):
        left_arr[i] = arr[low + i]
    for i in range(r_length):
        right_arr[i] = arr[mid + i + 1]

    i = 0
    j = 0
    k = low
    while i < l_length and j < r_length:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < l_length:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < r_length:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

if __name__ == "__main__":
