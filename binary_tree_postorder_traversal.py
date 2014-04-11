#!/usr/bin/env python

__author__ = 'Rio'

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def binary_tree_postorder(root):
    '''Traverse a binary tree in post order, which means traverse
    the left first, then right then root.'''
    if not root:
        return None

    result = []
    node_stack = [root]
    while node_stack:
        current = node_stack[-1]
        print current.val
        if current.left is not None: #Visit left node first
            node_stack.append(current.left)
        else:
            if current.right is not None: #Right node second
                node_stack.append(current.right)
            else: #Finally, root node
                result.append(current.val)
                node_stack.pop()

    return result

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c

    result = binary_tree_postorder(a)
    for r in result:
        print r,
