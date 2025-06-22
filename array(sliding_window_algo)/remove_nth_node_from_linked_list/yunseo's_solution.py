# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        current = head
        cnt = 0

        # lenght of the linked list
        while current:
            current = current.next
            cnt += 1

        current = dummy
        print(current)
        for _ in range(cnt - n):
            current = current.next
        
        # delete
        current.next = current.next.next
        
        return dummy.next