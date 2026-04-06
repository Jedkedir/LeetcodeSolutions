"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        curr = head
        while curr:
            if curr.child:
                nxt= curr.next
                child_head = curr.child
                child_tail = child_head
                while child_tail.next:
                    child_tail = child_tail.next
                curr.next = child_head
                child_head.prev = curr
                curr.child = None 
                if nxt:
                    child_tail.next = nxt
                    nxt.prev = child_tail
            curr = curr.next
        return head    