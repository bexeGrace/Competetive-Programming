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
