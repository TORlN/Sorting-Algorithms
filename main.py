from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shell_sort1 import shell_sort1
def insertion_sort_test():
    # Test case 1: Empty list
    arr = []
    assert insertion_sort(arr) == []

    # Test case 2: List with one element
    arr = [5]
    assert insertion_sort(arr) == [5]

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5]
    assert insertion_sort(arr) == [1, 3, 5, 7, 9]

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5]
    assert insertion_sort(arr) == [2, 2, 5, 5, 8]

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5]
    assert insertion_sort(arr) == [-7, -5, -4, -2, -1]

    print("Insertion Sort: PASSED")

def merge_sort_test():
    # Test case 1: Empty list
    arr = []
    assert merge_sort(arr) == []

    # Test case 2: List with one element
    arr = [5]
    assert merge_sort(arr) == [5]

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5]
    assert merge_sort(arr) == [1, 3, 5, 7, 9]

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5]
    assert merge_sort(arr) == [2, 2, 5, 5, 8]

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5]
    assert merge_sort(arr) == [-7, -5, -4, -2, -1]

    print("Merge Sort: PASSED")

def shell_sort_1_test():
    # Test case 1: Empty list
    arr = []
    assert shell_sort1(arr) == []

    # Test case 2: List with one element
    arr = [5]
    assert shell_sort1(arr) == [5]

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5]
    assert shell_sort1(arr) == [1, 3, 5, 7, 9]

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5]
    assert shell_sort1(arr) == [2, 2, 5, 5, 8]

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5]
    assert shell_sort1(arr) == [-7, -5, -4, -2, -1]

    print("Shell Sort 1: PASSED")

def main():
    insertion_sort_test()
    merge_sort_test()
    shell_sort_1_test()
if __name__ == "__main__":
    main()