#!/usr/bin/env python

__author__ = 'Rio'

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

def add_two_numbers(l1, l2):
    '''
    You are given two linked lists representing two non-negative numbers.
    The digits are stored in reverse order and each of their nodes contain a
    single digit. Add the two numbers and return it as a linked list.

    >>> add_two_numbers(2 -> 4 -> 3, 5 -> 6 -> 4)
    >>> 7 -> 0 -> 8
    '''
    if not l1 and not l2:
        return None

    head = ListNode(0)
    current, carry = head, 0

    while l1 and l2:
        value = l1.val + l2.val + carry
        carry = value / 10
        current.next = ListNode(value % 10)

        l1, l2, current = l1.next, l2.next, current.next

    while l1:
        value = l1.val + carry
        carry = value / 10
        current.next = ListNode(value % 10)
        l1, current = l1.next, current.next

    while l2:
        value = l2.val + carry
        carry = value / 10
        current.next = ListNode(value % 10)
        l2, current = l1.next, current.next

    if carry:
        current.next = ListNode(carry)

    return head.next
