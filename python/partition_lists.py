#!/usr/bin/env python

__author__ = 'Rio'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        Partition a linked list around value x and returns the head.

        Approach: Divide and Conquer - Merge Sort
        1. Divides the list into two halves around x.
        3. Merges the halves and updates the head pointer.

        Analysis:
        Time Complexity: O(NlogN), where N means the number of the given list.
        """
        if not head:
            return None

        before, after = self.split(head, x)
        node = self.merge(before, after)
        
        return node

    def split(self, head, x):
        """
        Returns two lists around x.

        Splits the nodes of given list into two halves before and after.
        """

        before.next = fast
        after.next = slow
        while head:
            if head.val <= x:
                fast.next = head
                fast = fast.next
            else:
                slow.next = head
                slow = slow.next
            head = head.next

        return (before.next, after.next)

    def merge(self, before, after):
        """
        Returns the new head of merged lists.
        """
        if not before:
            return after
        elif not after:
            return before

        current = before
        while current.next:
            current = current.next
        current.next = after

        return before
