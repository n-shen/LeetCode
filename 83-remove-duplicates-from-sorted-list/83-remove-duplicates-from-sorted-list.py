# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head, head
        
        while curr and curr.next:
            if curr.val != curr.next.val:
                prev.next = curr.next
                prev = curr.next
            
            curr = curr.next
        
        if prev:
            prev.next = None
        
        return head
    