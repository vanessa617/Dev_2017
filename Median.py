def median(nums):
    sort_nums = sorted(nums)
    len_nums = len(sort_nums)
    if len_nums % 2 == 0:
        return (sort_nums[int(len_nums/2 - 1)] + sort_nums[int(len_nums/2)])/2.0
    else:
        return (sort_nums[int(len_nums -1)/2])