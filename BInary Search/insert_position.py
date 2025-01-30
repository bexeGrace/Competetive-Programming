def searchInsert(self, nums, target):
    for index, value in enumerate(nums):
        if value >= target:
            return index
    return len(nums)

        