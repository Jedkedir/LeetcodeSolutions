# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        
        def post_order(node: Optional[TreeNode]) -> tuple[int, int]:
            nonlocal count
            if not node:
                return 0, 0
            left_sum, left_cnt = post_order(node.left)
            right_sum, right_cnt = post_order(node.right)
            total_sum = left_sum + right_sum + node.val
            total_cnt = left_cnt + right_cnt + 1
            if total_sum // total_cnt == node.val:
                count += 1
            return total_sum, total_cnt
        post_order(root)
        return count