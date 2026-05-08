# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous,current = None, head

        while current:
            temp = current.next
            current.next = previous
            previous = current
            print (previous.next)
            current = temp
        return previous
       

        # 0->1->2->3->4
        #head = 0, current = 0, previous = None
        #temp = current.next => temp = 1
        #current.next = previous => current.next = None
        #previous = current => previous = 0
        #current = temp => current = 1
        # None <- 0 

        # current = 1 current.next = 2
        #temp = 2 
        #current.next = 0
        #prev = 1
        #current = 2
        # None <- 0 <- 1 <- 2 <- 3(prev)
