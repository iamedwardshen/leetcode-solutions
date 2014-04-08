#!/usr/bin/env python

__author__ = 'Rio'

def valid(s):
    if not s: return None

    left = '([{'
    right = ')]}'

    stack = []
    for ele in s:
        if ele in left:
            stack.append(ele)
        else:
            if len(stack):
                opt = stack.pop()
            else:
                return False

            if left.index(opt) != right.index(ele):
                return False

    return True
