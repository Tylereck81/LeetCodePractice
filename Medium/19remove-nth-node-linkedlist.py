# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time Complexity: O(n) 
# Space Complexity: O(1)
def removeNthFromEnd(head, n):
    if head.next is None:
        head = None 
        return head

    end = head
    curr = head
    prev = head
    while end: 
        if n>0:
            n-=1
            end = end.next
        else: 
            end = end.next
            prev = curr
            curr = curr.next
        
    if curr == head: 
        head = head.next
        return head
    elif curr.next == 0: 
        prev.next = None 
        return head 
    else:   
        prev.next = curr.next 
        return head

def printl(head:ListNode): 
    while head: 
        print(head.val, end="") 
        head = head.next
    print() 

l = ListNode(1,ListNode(2,ListNode(3, ListNode(4, ListNode(5)))))
l2 = ListNode(1) 
printl(l2)

removeNthFromEnd(l2,1)
printl(l2)