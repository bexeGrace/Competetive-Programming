class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        fir = 0
        sec = fir + 1

        while sec < len(nums):
            if nums[fir] == nums[sec]:
                nums[fir] *= 2
                nums[sec] = 0
            fir += 1
            sec += 1
        
        zeros = nums.count(0)
        temp = list(filter(lambda x: x != 0, nums))
        temp = temp + [0] * zeros
        return temp
