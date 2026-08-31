# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        critical_indices = []
        prev = head
        curr = head.next
        idx = 1
        while curr.next:
            nxt = curr.next
            if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
                critical_indices.append(idx)
            prev = curr
            curr = nxt
            idx += 1
        if len(critical_indices) < 2:
            return [-1, -1]
        min_dist = float('inf')
        for i in range(1, len(critical_indices)):
            min_dist = min(min_dist, critical_indices[i] - critical_indices[i - 1])
        max_dist = critical_indices[-1] - critical_indices[0]
        return [min_dist, max_dist]