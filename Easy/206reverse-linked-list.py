# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head): 
    while head:
        print(head.val, end= " ") 
        head = head.next
    print()


def reverseList(head):
    l = [] 
    t = head
    while t: 
        l.append(t.val)
        t = t.next 
    l.reverse()
    c = 0
    t = head 
    
    while t: 
        t.val = l[c]
        c+=1
        t = t.next
    return head


def reverseList2(head): 
    prev = None 
    curr = head 

    while curr: 
        temp = curr
        curr = curr.next
        temp.next = prev
        prev = temp 

    head = prev
    return head


h1= ListNode(5,ListNode(4,ListNode(3,ListNode(2,ListNode(1)))))
reverseList(h1)
print_list(h1)
