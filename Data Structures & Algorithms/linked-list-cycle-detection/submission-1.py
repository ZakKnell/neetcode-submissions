# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast = head
        slow = head
        if not fast:
            return False

        while True:
            if fast.next is not None:
                fast = fast.next
                if fast.next is not None:
                    fast = fast.next
                else:
                    return False
            else:
                return False
            slow = slow.next
            if fast == slow:
                return True

