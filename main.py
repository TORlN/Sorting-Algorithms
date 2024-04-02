from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shell_sort1 import shell_sort1
from shell_sort2 import shell_sort2
from shell_sort3 import shell_sort3
from shell_sort4 import shell_sort4
def insertion_sort_test():
    # Test case 1: Empty list
    arr = []
    assert insertion_sort(arr) == []

    # Test case 2: List with one element
    arr = [5]
    assert insertion_sort(arr) == [5]

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    assert insertion_sort(arr) == [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    assert insertion_sort(arr) == [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

    print("Insertion Sort: PASSED")

def merge_sort_test():
    # Test case 1: Empty list
    arr = []
    assert merge_sort(arr) == []

    # Test case 2: List with one element
    arr = [5]
    assert merge_sort(arr) == [5]

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    assert merge_sort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    assert merge_sort(arr) == [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    assert merge_sort(arr) == [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

    print("Merge Sort: PASSED")

def shell_sort_1_test():
    # Test case 1: Empty list
    arr = []
    assert shell_sort1(arr) == []

    # Test case 2: List with one element
    arr = [5]
    assert shell_sort1(arr) == [5]

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    assert shell_sort1(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    assert shell_sort1(arr) == [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    assert shell_sort1(arr) == [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

    print("Shell Sort 1: PASSED")

def shell_sort_2_test():
    # Test case 1: Empty list
    arr = []
    assert shell_sort2(arr) == []

    # Test case 2: List with one element
    arr = [5]
    assert shell_sort2(arr) == [5]

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    assert shell_sort2(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    assert shell_sort2(arr) == [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    assert shell_sort2(arr) == [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

    print("Shell Sort 2: PASSED")

def shell_sort_3_test():
    # Test case 1: Empty list
    arr = []
    assert shell_sort3(arr) == []

    # Test case 2: List with one element
    arr = [5]
    assert shell_sort3(arr) == [5]

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    assert shell_sort3(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    assert shell_sort3(arr) == [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    assert shell_sort3(arr) == [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

    print("Shell Sort 3: PASSED")

def shell_sort_4_test():
    # Test case 1: Empty list
    arr = []
    assert shell_sort4(arr) == []

    # Test case 2: List with one element
    arr = [5]
    assert shell_sort4(arr) == [5]

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    assert shell_sort4(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    assert shell_sort4(arr) == [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    assert shell_sort4(arr) == [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

    print("Shell Sort 4: PASSED")
    
def main():
    insertion_sort_test()
    merge_sort_test()
    shell_sort_1_test()
    shell_sort_2_test()
    shell_sort_3_test()
    shell_sort_4_test()
if __name__ == "__main__":
    main()