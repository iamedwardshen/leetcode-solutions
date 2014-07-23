#!/usr/bin/env python

__author__ = 'Rio'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        Removes the Nth node from the end of the list and returns its head.

        We use a temporary dummy node as the start of the result list. So we could avoid painful
        removing operation.
        """
        if not head:
            return None

        dummy = ListNode(0)
        previous = dummy

        while n:
            if not head:
                return None
            head = head.next
            n -= 1

        while head:
            head = head.next
            previous = previous.next

        previous.next = previous.next.next

        return dummy.next

        
if __name__ == '__main__':
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    head.next = second
    #second.next = third

    solution = Solution()
    solution.removeNthFromEnd(head, 1)
    while head:
        print "%d" % head.val
        head = head.next
