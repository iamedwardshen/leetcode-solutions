#!/usr/bin/env python

__author__ = 'Rio'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def convert_array_bst(self, num):
        if not num:
            return None

        return self.build(num, 0, len(num)-1)

    def build(self, num, start, end):
        if start > end:
            return None

        mid = (start+end) / 2
        node = TreeNode(num[mid])
        node.left = self.build(num, start, mid-1)
        node.right = self.build(num, mid+1, end)

        return node
