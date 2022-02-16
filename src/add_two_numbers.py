from collections import deque

class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = result_tail = ListNode(0)

        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)


            carry, out = divmod(val1 + val2 + carry, 10)


            result_tail.next = ListNode(out)

            result_tail = result_tail.next

            l1 = (l1.next if l1.next else None)
            l2 = (l2.next if l2.next else None)

        return result.next

#l1 = [2,4,3], l2 = [5,6,4]



root1 = ListNode(2)
root1.next = ListNode(4)
root1.next.next = ListNode(3)

root2 = ListNode(5)
root2.next = ListNode(6)
root2.next.next = ListNode(4)

sol = Solution()

print(sol.addTwoNumbers(root1, root2))