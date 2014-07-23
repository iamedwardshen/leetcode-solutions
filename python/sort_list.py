#!/usr/bin/env python

__author__ = 'Rio'

class ListNode():
    '''List node object'''
    def __init__(self, x):
        self.val = x
        self.next = None

def sort_list(head):
    '''Sort a linked list on contant space and O(nlogn) time.'''
    if not head:
        return 0

    #Calculate the length of the list.
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next

    mid = length / 2


if __name__ == '__main__':
    a = ListNode(2)
    print sort_list(a)
