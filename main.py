from insertion_sort import insertion_sort
from merge_sort import merge_sort
import random
def insertion_sort_test():
    nums = [random.randint(1, 100) for _ in range(10)]
    sortedNums = sorted(nums)
    nums = insertion_sort(nums)
    if nums == sortedNums:
        print("insertion_sort PASSED")
    else:
        print("insertion_sort FAILED")
        print(f"Expected: {sortedNums}")
        print(f"Got: {nums}")
def merge_sort_test():
    nums = [random.randint(1, 100) for _ in range(10)]
    sortedNums = sorted(nums)
    nums = merge_sort(nums)
    if nums == sortedNums:
        print("merge_sort PASSED")
    else:
        print("merge_sort FAILED")
        print(f"Expected: {sortedNums}")
        print(f"Got: {nums}")
def main():
    insertion_sort_test()
    merge_sort_test()
    
if __name__ == "__main__":
    main()