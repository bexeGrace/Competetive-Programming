def hasCycle(head):
    slow = head
    fast = head
    while slow is not None and fast is not None:
        slow = slow.next
        if fast.next is not None:
            fast = fast.next.next
        else: 
            return False
        if fast == slow:
            return True

    return False