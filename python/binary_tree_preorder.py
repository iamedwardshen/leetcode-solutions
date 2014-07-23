#!/usr/bin/env python

__author__ = 'Rio'


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []

        result = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

if __name__ == '__main__':
    root = Node(1)
    left = Node(4)
    right = Node(3)
    node = Node(2)
    
    root.left = left
    root.right = right
    right.left = node
    solution = Solution()
    result = solution.preorderTraversal(root)
    for ele in result:
        print ele,
    print
