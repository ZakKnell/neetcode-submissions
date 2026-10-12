# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        lengthNode = head
        while lengthNode.next != None:
            lengthNode = lengthNode.next
            length += 1

        removeNode = length - n 

        if removeNode == 0:
            return head.next
            
        dummy = head
        current = head
        for i in range(removeNode - 1):
            current = current.next
        temp = current.next
        current.next = temp.next

        return dummy

        