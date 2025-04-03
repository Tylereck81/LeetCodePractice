# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printl(head: ListNode): 
    while head: 
        print(head.val, end= " ")
        head = head.next
    print()

def swapPairs(head: ListNode) -> ListNode:
    if head == None or head.next == None: 
            return head 

    one = head 
    two = head.next
    prev = None

    while one and two:    
            
        if one == head: 
            one.next = two.next
            two.next = one
            head = two 
        else: 
            one.next = two.next
            two.next = one
            prev.next = two 

        # Swap One and Two
        temp = one 
        one = two 
        two = temp

        prev = two
        one = None if one.next.next is None else one.next.next
        two = two.next.next if two.next is not None else None  

    return head

l1 = ListNode(1,ListNode(2,ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
printl(l1)
l1 = swapPairs(l1) 
printl(l1)
