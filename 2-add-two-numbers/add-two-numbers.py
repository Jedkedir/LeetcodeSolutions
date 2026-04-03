class Solution:
    def addTwoNumbers(self, ptr1: Optional[ListNode], ptr2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while ptr1 or ptr2 or carry:
            vaptr1 = ptr1.val if ptr1 else 0
            vaptr2 = ptr2.val if ptr2 else 0
            total = vaptr1 + vaptr2 + carry
            carry = total // 10
            new_digit = total % 10
            curr.next = ListNode(new_digit)
            curr = curr.next
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
        return dummy.next