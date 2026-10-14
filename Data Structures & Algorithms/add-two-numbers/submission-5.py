# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = dummy = ListNode()
        carry = 0

        while l1 or l2 or carry:
            l1Value = l1.val if l1 else 0
            l2Value = l2.val if l2 else 0

            temp = l1Value + l2Value + carry

            current = temp % 10
            carry = temp // 10

            l3.next = ListNode(current)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            l3 = l3.next

        return dummy.next

            
