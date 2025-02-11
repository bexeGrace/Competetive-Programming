from typing import List


def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    sumn = 0
    for i in range(len(nums)//2):
        if i == 0:
            sumn += nums[i]
        else:
            sumn += nums[2*i]
    
    return sumn


print(arrayPairSum([1,4,3,2]))