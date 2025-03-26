def removeElements(head, val):
    if head == 0:
        return head
    t = head 
    prev = head
    while t: 
        if t.val == val: 
            
            if t == head: 
                head = t.next 
            elif t.next == 0: 
                prev.next = 0
            else: 
                prev.next = t.next 
            t = t.next
        else: 
            prev = t 
            t = t.next

    return head
        