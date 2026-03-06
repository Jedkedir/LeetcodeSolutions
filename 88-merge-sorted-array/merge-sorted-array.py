class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr = len(nums1) - 1
        p1, p2 = m - 1, n - 1
        while p2 >= 0:
            if p1 < 0 or nums2[p2] >= nums1[p1]:
                nums1[ptr] = nums2[p2]
                p2 -= 1
            else:
                nums1[ptr] = nums1[p1]
                p1 -= 1
            ptr -= 1