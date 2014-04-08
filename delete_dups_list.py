#!/usr/bin/env python

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
        def deleteDuplicates(self, head):
            if not head:
                return head
            current = head
            content = {current.val: True}
            while current.next:
                if current.next.val in content:
                    current.next = current.next.next
                else:
                    content[current.next.val] = True
                    current = current.next
            return head

if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)

    temp = a
    while temp:
        print temp.val,
        temp = temp.next
    print

    s = Solution()
    temp = s.deleteDuplicates(a)
    while temp:
        print temp.val,
        temp = temp.next
    print
