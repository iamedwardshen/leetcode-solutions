#!/usr/bin/env python

__author__ = 'Rio'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def convert_array_bst(self, num):
        """ Converts a sorted array to a binary search tree.

        Approach:
        Utilizes BST definition - the left node is no greater than
        the root and right is no less than the root. So the root should be
        the middle element in the array, left child should be the mid of left
        half and so on.

        This pattern is easily to found and works fine using Divide and Conquer.
        """
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
