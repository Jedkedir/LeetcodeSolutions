# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n, curr = 0, head
        while curr:
            n += 1
            curr = curr.next
        width, remainder = divmod(n, k)
        res = []
        curr = head
        for i in range(k):
            part_head = curr
            size = width + (1 if i < remainder else 0)
            for _ in range(size - 1):
                if curr: 
                    curr = curr.next
            if curr:
                temp = curr.next
                curr.next = None
                curr = temp
            res.append(part_head)
        return res
            