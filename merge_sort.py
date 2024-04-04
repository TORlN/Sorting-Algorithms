def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    merge(arr, left_half, right_half)


def merge(arr, left, right):
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[i + j] = left[i]
            i += 1
        else:
            arr[i + j] = right[j]
            j += 1

    while i < len(left):
        arr[i + j] = left[i]
        i += 1

    while j < len(right):
        arr[i + j] = right[j]
        j += 1
