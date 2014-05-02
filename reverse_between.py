#!/usr/bin/env python

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        if not head:
            return None

        step = n-m
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy

        pre = head
        while m > 1:
            pre = pre.next
            m -= 1
        cur = pre.next
        pos = cur.next

        if step > 1:
            while step > 0 and pos is not None:
                temp = pos.next
                pos.next = cur
                cur = pos
                post = temp
                step -= 1
            temp = pre.next
            pre.next = cur
            temp.next = pos
        dummy = head
        head = head.next
        return head

if __name__ == '__main__':
    a, b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    temp = a
    while temp:
        print temp.val,
        temp = temp.next
    print

    temp = a
    solution = Solution()
    temp = solution.reverseBetween(temp, 2, 4)
    while temp:
        print temp.val,
        temp = temp.next
    print

    
