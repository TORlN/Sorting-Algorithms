import math

def shell_sort2(nums):
    n = len(nums)
    if n == 0:
        return nums

    k = int(math.log(n, 2))
    sequence = []
    for i in range(k):
        if i == 0:
            sequence.append(1)
        else:
            sequence.append(2 ** i +1 )
            
            
    for gap in sequence:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
    return nums

