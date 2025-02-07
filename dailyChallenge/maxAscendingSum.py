class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        summ = nums[0]
        max_sum = summ
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                if summ > max_sum:
                    max_sum = summ
                summ = nums[i+1]
            else:
                summ += nums[i+1]
        if summ > max_sum:
            max_sum = summ
        return max_sum