class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode):
    lista = headA
    listb = headB

    while lista != listb:
        lista = lista.next if lista else headB
        listb = listb.next if listb else headA
    
    return listb


A = ListNode(4)
A2 = ListNode(1)
A3 = ListNode(8)
A4 = ListNode(4)
A5 = ListNode(5)
A.next = A2
A2.next = A3
A3.next = A4
A4.next = A5

B = ListNode(5)
B2 = ListNode(6)
B3 = ListNode(1)
B4 = ListNode(8)
B5 = ListNode(4)
B6 = ListNode(5)
B.next = B2
B2.next = B3
B3.next = A3


print(getIntersectionNode(A, B))