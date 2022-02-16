# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        prev, current = dummy, head

        while current and current.next:

            nextPair = current.next.next
            second = current.next

            second.next = current
            prev.next = second
            current.next = nextPair

            prev = current
            current = nextPair

        return dummy.next


#head = [1,2,3,4]

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

sol = Solution()

print(sol.swapPairs(head))