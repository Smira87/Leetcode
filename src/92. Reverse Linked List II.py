from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        def reverseList(head):
            cur = head
            tail = None
            while cur:
                tail = ListNode(cur.val, tail)
                cur = cur.next
            return tail

        count = 1
        cur = head
        dummy = ListNode(-1)
        prev = ListNode(-1)
        while count < left:
            if not cur.next:
                print("Left index is out of range")
                return
            if count == left - 1:
                prev = cur

            cur = cur.next
            count += 1
        new_head = dummy.next = ListNode(cur.val)

        if right == left:
            return head
        while count < right + 1:
            if not cur:
                print("Right index is out of range")
                return
            dummy.next.next = ListNode(cur.val)
            next = cur.next
            cur = cur.next
            dummy = dummy.next
            count += 1

        res = reverseList(new_head.next)
        cur = head
        prev.next = res
        while cur.next:
            cur = cur.next
        cur.next = next
        return head