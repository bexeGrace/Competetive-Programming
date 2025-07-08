from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        if not list2:
            return list1

        # Recursive case: pick the smaller head and recurse
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        curr = len(nums1) - 1
        i, j = m-1, n-1
        if m == 0 or n == 0:
            if n > 0:
                nums1 = nums2
            else:
                nums1 = nums1[:m] 
        else:
            while i >= 0 or j >= 0:
                if nums1[i] >= nums2[j]:
                    nums1[curr] = nums1[i]
                    i -= 1
            
                else:
                    nums1[curr] = nums2[j]
                    j -= 1
                curr -= 1
                if i < 0 or j < 0:
                    break
        
        print(nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sol = Solution()
sol.merge(nums1, 3, nums2, 3)    