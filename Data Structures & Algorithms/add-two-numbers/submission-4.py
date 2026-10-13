# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = dummy = ListNode()

        while l1 or l2:
            if not l1:
                temp = l2.val
            elif not l2:
                temp = l1.val
            else:
                temp = l1.val + l2.val

            if l3.val:
                total = temp + l3.val
            else:
                total = temp

            if total < 10:
                l3.val = total
            else:
                l3.val = total - 10
                l3.next = ListNode()
                l3.next.val = 1

            if l2:
                l2 = l2.next
            if l1:
                l1 = l1.next
            if (l1 or l2) and not l3.next:
                l3.next = ListNode()
            l3 = l3.next

        return dummy
            
            


        
