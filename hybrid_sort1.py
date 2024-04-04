from insertion_sort import insertion_sort

def hybrid_sort1(arr):
    H = len(arr) ** .2
    return h_sort(arr, H)

def h_sort(arr, H):
    if len(arr) <= 1:
        return arr
    if len(arr) > H:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        left_half = h_sort(left_half, H)
        right_half = h_sort(right_half, H)
        
        return merge(left_half, right_half) 
    else:
        return insertion_sort(arr)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result