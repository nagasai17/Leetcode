# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # c=c1=c2=head
        # while(c1.next and c2.next):
        #     c=head
        #     c1=head.next
        #     c2=head.next.next
        #     head=head.next
        # return c
        c=c1=head
        while(c1 and c1.next):
            c=c.next
            c1=c1.next.next
        return c    
            
        
