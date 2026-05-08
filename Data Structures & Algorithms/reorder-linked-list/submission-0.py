# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head.next
       

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next, previous = None, None
        #1 2 3 | 4 5
        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp
        #1 -> 2 ->(slow) 3 ->(slow.next) Null | Null<- 4 (second.next)<- 5(second)
        curr = head
        second = previous
        while second:
            temp1,temp2 = curr.next,second.next
            curr.next = second
            second.next = temp1
            curr,second = temp1,temp2

        