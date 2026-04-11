class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        m = {}
        for num in nums2:
            while stack and num > stack[-1]:
                smaller_num = stack.pop()
                m[smaller_num] = num
            stack.append(num)
        return [m.get(n, -1) for n in nums1]