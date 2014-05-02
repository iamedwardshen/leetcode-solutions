#!/usr/bin/env python

__author__ = 'Rio'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def remove(self, head):
        if not head:
            return None

        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
