#!/usr/bin/env python

__author__ = 'Rio'

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    if not head:
        return False

    slow = fast = head
    
    while True:
        slow = slow.next

        if not fast.next:
            return False
        else:
            fast = fast.next.next

        if not fast or not slow:
            return False

        if slow == fast:
            return True

if __name__ == '__main__':
    head = ListNode(1)
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(4)
    head.next = a
    a.next = b
    b.next = c
    c.next = None

    print has_cycle(head)
