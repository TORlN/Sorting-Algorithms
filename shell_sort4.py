def shell_sort4(nums):
    n = len(nums)
    if n == 0:
        return nums
    sequence = [1, 8, 23, 77, 281, 1073, 4193, 16577, 65921, 262913, 1050113, 4197377, 16783361, 67121153, 268460033, 1073790977, 4295065601, 17180065793, 68719869953, 274878693377, 1099513200641, 4398049656833, 17592192335873, 70368756760577]
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