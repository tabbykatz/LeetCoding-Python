# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = head
        counter = 1
   
        while head:
            if counter % 2 == 0:
                mid = mid.next
            head = head.next
            counter += 1
        return mid


            

        
            