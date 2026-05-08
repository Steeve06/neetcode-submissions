# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        dummy = current
        count = 0
        while current and count < k :
            count += 1
            current = current.next
        if count < k :
            return head

        prev,current = None, head
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        dummy.next = self.reverseKGroup(current,k)

        return prev
 
         