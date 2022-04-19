# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        digit_sum = ListNode(val = (l1.val + l2.val) % 10)  # remainder
        carry = (l1.val + l2.val) // 10 # carry over
        cur_node = digit_sum
        
        while l1.next or l2.next:
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
                cur_node.next = ListNode(val = (l1.val + l2.val + carry) % 10)
                carry = (l1.val + l2.val + carry) // 10
                cur_node = cur_node.next
            elif l1.next:
                while l1.next:
                    l1 = l1.next
                    cur_node.next = ListNode(val = (l1.val + carry) % 10)
                    carry = (l1.val + carry) // 10
                    cur_node = cur_node.next
            else:
                while l2.next:
                    l2 = l2.next
                    cur_node.next = ListNode(val = (l2.val + carry) % 10)
                    carry = (l2.val + carry) // 10
                    cur_node = cur_node.next
                
        if carry > 0:
            cur_node.next = ListNode(val = 1)
            
        return digit_sum
            