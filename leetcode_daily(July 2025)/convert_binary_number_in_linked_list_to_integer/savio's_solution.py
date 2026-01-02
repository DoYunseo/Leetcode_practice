from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current = head
        m_string = ""

        while current:
            m_string += str(current.val)
            current = current.next
        return int(m_string, 2)
        