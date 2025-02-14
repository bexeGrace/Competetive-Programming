from typing import List

def minOperations(nums: List[int], k: int) -> int:
    import heapq

    count = 0
    heapq.heapify(nums)

    while nums[0] < k and len(nums) >= 2:
        first = heapq.heappop(nums)
        second = heapq.heappop(nums)
        res = first * 2 + second
        heapq.heappush(nums, res)
        count += 1

    return count




