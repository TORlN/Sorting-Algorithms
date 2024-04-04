from insertion_sort import insertion_sort

def hybrid_sort2(arr):
    H = len(arr) ** .4
    h_sort(arr, H)

def h_sort(arr, H):
    if len(arr) <= 1:
        return
    if len(arr) > H:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        h_sort(left_half, H)
        h_sort(right_half, H)
        
        merge(arr, left_half, right_half) 
    else:
        insertion_sort(arr)

def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1