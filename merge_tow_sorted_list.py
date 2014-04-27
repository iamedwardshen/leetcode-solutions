#!/usr/bin/env python

__author__ = 'Rio'

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def mergeTwoLists(self, l1, l2):
        """
        Return a merged linked list.

        Iterate through two lists while comparing them.
        We take care of special cases such as different lengths.
        """
        head = Node(0)
        current = head
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return head.next

if __name__ == '__main__':
    l1 = Node(1)
    l2 = Node(2)
    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)
    while result:
        print result.val
        result = result.next
