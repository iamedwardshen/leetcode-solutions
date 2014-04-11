#!/usr/bin/env python

__author__ = 'Rio'

def is_balanced(root):
    return False if check_height(root) == -1 else True

def check_height(root):
    if not root:
        return 0

    left = check_height(root.left)
    if left == -1:
        return -1

    right = check_height(root.right)
    if right == -1:
        return -1

    if abs(left - right) > 1:
        return -1

    return max(left, right) + 1
