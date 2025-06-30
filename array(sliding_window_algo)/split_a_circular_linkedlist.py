def split_circular_linked_list(head):
    slow = fast = head
  
    while fast.next != head and fast.next.next != head:
      slow = slow.next
      fast = fast.next.next
  
    head1 = head
    head2 = slow.next
    slow.next = head1 
    
    fast = head2
    while fast.next != head:
      fast = fast.next
    fast.next = head2  
  
    return [head1, head2]
