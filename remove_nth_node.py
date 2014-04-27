#!/usr/bin/env python

__author__ = 'Rio'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        Remove nth from the end node from the linked list.

        We split the whole list into two part with length K and N.
        Our target is to remove the Nth element from the head.
        To do this, we use fast runner approach. Iterate N element using
        fast pointer, so there're K elements rest.
        Then, start to run slow pointer from head while running fast to
        attach the end.
        """
        fast, slow = head, head

        while n != 0:
            if fast:
                fast = fast.next
            else: # n is greater than the length of list.
                return

        while fast:
            slow = slow.next
            fast = fast.next

        return slow
