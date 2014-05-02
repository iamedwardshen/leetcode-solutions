#!/usr/bin/env python

__author__ = 'Rio'

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def mergeTwoLists(self, l1, l2):
        """
        Return a merged linked list in increasing order.

        Approach
        Use a temporary dummy node as the start of the result list. The next pointer always
        points to the last node in the result list, so appending new node is easy.
        The loop proceeds, removing one node from either l1 or l2, and adding it to the tail.
        When we are done, the result is in dummy.next

        Analysis:
        hTime Complexity: O(N), where N means the number of nodes in the list.

        """
        dummy = Node(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next


        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next

if __name__ == '__main__':
    l1 = Node(1)
    l2 = Node(2)
    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)
    while result:
        print result.val
        result = result.next
