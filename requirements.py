# Import each one of your sorting algorithms below as follows:
# Feel free to comment out these lines before your algorithms are implemented.
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shell_sort1 import shell_sort1
from shell_sort2 import shell_sort2
from shell_sort3 import shell_sort3
from shell_sort4 import shell_sort4
from hybrid_sort1 import hybrid_sort1
from hybrid_sort2 import hybrid_sort2
from hybrid_sort3 import hybrid_sort3

# Please read the below carefully:

# - Each sorting algorithm should be implemented in its own file.
# - No file should include anything outside of standard Python libraries.
# - Functions should be tested using Python 3.6+ on a Linux environment.
# - Each function should modify the input list so that it is sorted upon completion.

# Note:
#   If your Shellsort and/or hybrid merge sort variants largely use the same code,
#   you may choose to implement them in a single file, and import them as follows:
# from shell_sort import shell_sort1, shell_sort2, shell_sort3, shell_sort4
# from hybrid_sort import hybrid_sort1, hybrid_sort2, hybrid_sort3


def insertion_sort_test():
    # Test case 1: Empty list
    arr = []
    arrSorted = sorted(arr)
    insertion_sort(arr)
    assert arr == arrSorted

    # Test case 2: List with one element
    arr = [5]
    arrSorted = sorted(arr)
    insertion_sort(arr)
    assert arr == arrSorted

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    arrSorted = sorted(arr)
    insertion_sort(arr)
    assert arr == arrSorted

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    arrSorted = sorted(arr)
    insertion_sort(arr)
    assert arr == arrSorted

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    arrSorted = sorted(arr)
    insertion_sort(arr)
    assert arr == arrSorted

    print("Insertion Sort: PASSED")

def merge_sort_test():
    # Test case 1: Empty list
    arr = []
    merge_sort(arr)
    assert arr == []

    # Test case 2: List with one element
    arr = [5]
    merge_sort(arr)
    assert arr == [5]

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    arrSorted = sorted(arr)
    merge_sort(arr)
    assert arr == arrSorted

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    arrSorted = sorted(arr)
    merge_sort(arr)
    assert arr == arrSorted 

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    arrSorted = sorted(arr)
    merge_sort(arr)
    assert arr == arrSorted 

    print("Merge Sort: PASSED")

def shell_sort_1_test():
    # Test case 1: Empty list
    arr = []
    arrSorted = sorted(arr)
    shell_sort1(arr)
    assert arr == arrSorted

    # Test case 2: List with one element
    arr = [5]
    arrSorted = sorted(arr)
    shell_sort1(arr)
    assert arr == arrSorted

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    arrSorted = sorted(arr)
    shell_sort1(arr)
    assert arr == arrSorted

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    arrSorted = sorted(arr)
    shell_sort1(arr)
    assert arr == arrSorted

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    arrSorted = sorted(arr)
    shell_sort1(arr)
    assert arr == arrSorted

    print("Shell Sort 1: PASSED")

def shell_sort_2_test():
    # Test case 1: Empty list
    arr = []
    arrSorted = sorted(arr)
    shell_sort2(arr)
    assert arr == arrSorted

    # Test case 2: List with one element
    arr = [5]
    arrSorted = sorted(arr)
    shell_sort2(arr)
    assert arr == arrSorted

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    arrSorted = sorted(arr)
    shell_sort2(arr)
    assert arr == arrSorted

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    arrSorted = sorted(arr)
    shell_sort2(arr)
    assert arr == arrSorted

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    arrSorted = sorted(arr)
    shell_sort2(arr)
    assert arr == arrSorted

    print("Shell Sort 2: PASSED")

def shell_sort_3_test():
    # Test case 1: Empty list
    arr = []
    arrSorted = sorted(arr)
    shell_sort3(arr)
    assert arr == arrSorted

    # Test case 2: List with one element
    arr = [5]
    arrSorted = sorted(arr)
    shell_sort3(arr)
    assert arr == arrSorted

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    arrSorted = sorted(arr)
    shell_sort3(arr)
    assert arr == arrSorted

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    arrSorted = sorted(arr)
    shell_sort3(arr)
    assert arr == arrSorted

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    arrSorted = sorted(arr)
    shell_sort3(arr)
    assert arr == arrSorted

    print("Shell Sort 3: PASSED")

def shell_sort_4_test():
    # Test case 1: Empty list
    arr = []
    arrSorted = sorted(arr)
    shell_sort4(arr)
    assert arr == arrSorted

    # Test case 2: List with one element
    arr = [5]
    arrSorted = sorted(arr)
    shell_sort4(arr)
    assert arr == arrSorted

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    arrSorted = sorted(arr)
    shell_sort4(arr)
    assert arr == arrSorted

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    arrSorted = sorted(arr)
    shell_sort4(arr)
    assert arr == arrSorted

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    arrSorted = sorted(arr)
    shell_sort4(arr)
    assert arr == arrSorted

    print("Shell Sort 4: PASSED")

def hybrid_sort1_test():
    # Test case 1: Empty list
    
    arr = []
    arrSorted = sorted(arr)
    hybrid_sort1(arr)
    assert arr == arrSorted

    # Test case 2: List with one element
    arr = [5]
    arrSorted = sorted(arr)
    hybrid_sort1(arr)
    assert arr == arrSorted

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    arrSorted = sorted(arr)
    hybrid_sort1(arr)
    assert arr == arrSorted

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    arrSorted = sorted(arr)
    hybrid_sort1(arr)
    assert arr == arrSorted

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    arrSorted = sorted(arr)
    hybrid_sort1(arr)
    assert arr == arrSorted

    print("Hybrid Sort 1: PASSED")

def hybrid_sort2_test():
    # Test case 1: Empty list
    arr = []
    arrSorted = sorted(arr)
    hybrid_sort2(arr)
    assert arr == arrSorted

    # Test case 2: List with one element
    arr = [5]
    arrSorted = sorted(arr)
    hybrid_sort2(arr)
    assert arr == arrSorted

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    arrSorted = sorted(arr)
    hybrid_sort2(arr)
    assert arr == arrSorted

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    arrSorted = sorted(arr)
    hybrid_sort2(arr)
    assert arr == arrSorted

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    arrSorted = sorted(arr)
    hybrid_sort2(arr)
    assert arr == arrSorted

    print("Hybrid Sort 2: PASSED")

def hybrid_sort3_test():
     # Test case 1: Empty list
    arr = []
    arrSorted = sorted(arr)
    hybrid_sort3(arr)
    assert arr == arrSorted

    # Test case 2: List with one element
    arr = [5]
    arrSorted = sorted(arr)
    hybrid_sort3(arr)
    assert arr == arrSorted

    # Test case 3: List with multiple elements
    arr = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10, 15, 12, 11, 14, 13]
    arrSorted = sorted(arr)
    hybrid_sort3(arr)
    assert arr == arrSorted

    # Test case 4: List with duplicate elements
    arr = [5, 2, 8, 2, 5, 1, 3, 4, 6, 7, 9, 10, 11, 12, 13]
    arrSorted = sorted(arr)
    hybrid_sort3(arr)
    assert arr == arrSorted

    # Test case 5: List with negative numbers
    arr = [-4, -2, -7, -1, -5, -3, -6, -8, -9, -10, -11, -12, -13, -14, -15]
    arrSorted = sorted(arr)
    hybrid_sort3(arr)
    assert arr == arrSorted

    print("Hybrid Sort 3: PASSED")

    
insertion_sort_test()
merge_sort_test()
shell_sort_1_test()
shell_sort_2_test()
shell_sort_3_test()
shell_sort_4_test()
hybrid_sort1_test()
hybrid_sort2_test()
hybrid_sort3_test()
