class ListNode(object): 
    def __init__(self, val = 0, next = None): 
        self.val = val 
        self.next = next 

# Time Complexity is O(n), Space is O(1)
def deleteDuplicates(head):
    if head is None: return head
    if head.next is None: return head

    t1 = head
    t2 = head.next

    while t1: 
        while  t2 and t1.val == t2.val: 
            t2 = t2.next
        
        t1.next = t2
        t1 =  t2
    
    temp = head 
    while temp: 
        print(temp.val) 
        temp = temp.next

    return head

# Same Attempt but use one pointer (a little slower for some reason)
def deleteDuplicates2(head): 
    current = head 

    while current and current.next: 
        if current.val == current.next.val: 
            current.next = current.next.next
        else: 
            current = current.next
    
    return head

l1 = ListNode(1) 
l1.next = ListNode(1)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(3)
l1.next.next.next.next = ListNode(3)

deleteDuplicates(l1) # 1 -> 2 -> 3  


