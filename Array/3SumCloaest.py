from typing import List

def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_diff = float('inf')
        is_positive = False
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if abs(target - three_sum) < closest_diff:
                    closest_diff = abs(target - three_sum)
                    if target - three_sum <= 0:
                        is_positive = True
                    else:
                        is_positive = False

                if three_sum < target:
                    l += 1

                else:
                    r -= 1
        
        return target + closest_diff if is_positive else target - closest_diff