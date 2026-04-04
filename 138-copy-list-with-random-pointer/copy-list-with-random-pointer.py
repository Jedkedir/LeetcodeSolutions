"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        while curr:
            temp = Node(curr.val, curr.next)
            curr.next = temp
            curr = temp.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head
        dummy = Node(0)
        copy = dummy
        while curr:
            copy.next = curr.next
            copy = copy.next
            curr.next = curr.next.next
            curr = curr.next
        return dummy.next  