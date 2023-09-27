from typing import List

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if index == i:
                return cur.val
            i += 1
            cur = cur.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while cur.next:
            if index == i:
                cur.next = cur.next.next
                return True
            i += 1
            cur = cur.next
        return False

    def getValues(self) -> List[int]:
        cur = self.head.next
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

MyList = LinkedList()
MyList.insertHead(4)
MyList.insertHead(3)
MyList.insertHead(2)
MyList.insertHead(1)
MyList.remove(4)

print(MyList.getValues())