def shell_sort3(nums):
    n = len(nums)
    if n == 0:
        return nums
    sequence = [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, 81, 96, 108, 128, 144, 162, 192, 216, 243, 256, 288, 324, 384, 432, 486, 512, 576, 648, 729, 768, 864, 972, 1024, 1152, 1296, 1458, 1536, 1728, 1944, 2048, 2187, 2304, 2592, 2916, 3072, 3456, 3888]
    if sequence[-1] < n: # Generate more sequence values if needed
        for p in range(3888, n):
            for q in range(3888, n):
                val = (3 ** p) * (2 ** q)
                if val < n:
                    sequence.append(val)
                else:
                    break
        sequence.sort()
    else:
        sequence = [gap for gap in sequence if gap < n]
    sequence.reverse()
    for gap in sequence:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
    return nums