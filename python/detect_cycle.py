#!/usr/bin/env python

__author__ = 'Rio'

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


def detect_cycle(head):
    if not head:
        return None

    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
