#!/usr/bin/env python

__author__ = 'Rio'

def remove_element(A, elem):
    if not A: return None

    while elem in A:
        A.remove(elem)

    return len(A)

def remove_elem(A, elem):
    if not A: return None

    index = 0
    for i in xrange(1, len(A)):
        if elem != A[i]:
            A[index] = A[i]
            index += 1

    return index

a = [3, 3]
print remove_element(a, 3)
print a

a = [2]
print remove_elem(a, 3)
print a
