# https://www.algoexpert.io/questions/sum-of-linked-lists

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def sumHelper(linkedList, currDigit = 1):
    if linkedList.next is None:
        return currDigit * linkedList.value
        
    return (currDigit * linkedList.value) + sumHelper(linkedList.next, currDigit = currDigit*10)
    
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    total = sumHelper(linkedListOne) + sumHelper(linkedListTwo)
    temp = LinkedList(None)
    head = temp
    for digit in reversed(str(total)):
        temp.next = LinkedList(int(digit))
        temp = temp.next
    return head.next