# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        while head :
            values.insert(0, head.val)
            head = head.next
        
        ll = ListNode(0)
        cur = ll
        for val in values:
            cur.next = ListNode(val)
            cur = cur.next
        
        return ll.next


        