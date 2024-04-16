import math

def shell_sort2(nums):
    n = len(nums)
    if n == 0:
        return nums

    k = int(math.log(n, 2))
    sequence = [1, 3, 5, 9, 17, 33, 65, 129, 257, 513, 1025, 2049, 4097, 8193, 16385, 32769, 65537, 131073, 262145, 524289, 1048577, 2097153, 4194305, 8388609, 16777217, 33554433, 67108865, 134217729, 268435457, 536870913, 1073741825, 2147483649]
    sequence = sequence[:k]
    pass
    for gap in reversed(sequence):
        for i in range(gap, n):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
    return nums

