from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insert(self, root, value):
        if not root:
            return TreeNode(value)
        if value < root.val:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        head = TreeNode(nums[0])
        for i in range(len(nums) - 1, 0, -1):
            self.insert(head, nums[i])

        print(head.val)
        return head


nums = [-10,-3,0,5,9]

sol = Solution()

print(sol.sortedArrayToBST(nums).left)

