class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.value
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val, self.head.next)
        self.head.next = new_head
        if new_head.next == None:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val)
        self.tail.next = new_tail
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        curr = self.head.next
        i = 0
        prev = self.head
        while curr:
            if i == index:
                prev.next = curr.next
                if prev.next == None:
                    self.tail = prev
                return True
            else:
                i += 1
                prev = curr
                curr = curr.next
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res
        
class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next