from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        l = dummy
        r = head
        for i in range(n):
            r = r.next
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next
    def show(self, head):
        cur = head
        res = ""
        while cur:
            res = res + str(cur.val) + "->"
            cur = cur.next
        return res
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
sol = Solution()
print(sol.show(node1))
sol.removeNthFromEnd(node1, 2)
print(sol.show(node1))