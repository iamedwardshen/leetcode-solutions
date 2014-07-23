#!/usr/bin/env python

__author__ = 'Rio'

def remove_dups(A):
    if not A: return A

    slow = 0
    while slow < len(A):
        faster = slow + 1
        while faster < len(A):
            if A[faster] == A[slow]:
                del A[faster]
            faster += 1
        slow += 1

    return len(A)

a = [1, 1, 2]
print remove_dups(a)
for ele in a:
    print ele,
a = []
print remove_dups(a)
