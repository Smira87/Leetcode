# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)
class MyLinkedList(object):

    def __init__(self):
        self.head = None
    def length(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next

        return count
    def print_list(self):
        cur = self.head
        output = ""
        while cur:
            output += str(cur.val) + "-->"
            cur = cur.next
        print(output)
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        cur = self.head
        count = 0
        if index > self.length() - 1:
            print("Out of range")
            return -1
        while count != index:
            count += 1
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        cur = ListNode(val, self.head)
        self.head = cur

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head == None:
            self.head = ListNode(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        cur = self.head
        count = 0
        if index == 0 :
            self.addAtHead(val)
            return
        elif index > self.length():
            print("Index out of range")
            return -1
        elif index == self.length():
            self.addAtTail(val)
            return
        while count != index - 1:
            count += 1
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node




    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        count = 0
        cur = self.head
        if index > self.length() - 1:
            print("Index out of range")
            return -1
        elif index == 0:
            self.head = self.head.next
            return
        while count != index - 1:
            count += 1
            cur = cur.next
        cur.next = cur.next.next
        
obj = MyLinkedList()

obj.addAtHead(1)
obj.addAtTail(3)
#obj.addAtIndex(1, 2)
obj.print_list()

