#!/usr/bin/env python

__author__ = 'Rio'


def valid(s):
    """
    Solution:
    If a single element belongs to left parentheses,
    push it onto the stack, otherwise compare it with the top
    element in the stack -- this is because the right parentheses should
    be paired with the most recent left pair.
    Finally, the stack should be empty.

    Analysis:
    Time Complexity - O(N), where N means the elements in the string.
    Space Complexity - O(1), no additional spaces is needed.
    """
    if s is None:  # empty string is valid parentheses.
        return True

    left = set('([{')
    stack = []
    for element in s:
        if element in left:  # in operation of a set, holds a constant time
            stack.append(element)
        else:
            if len(stack) != 0 and is_valid(stack[-1], element):
                stack.pop()
            else:
                return False

    return not stack


def is_valid(left, right):
    return (left == '(' and right == ')'
            or left == '[' and right == ']'
            or left == '{' and right == '}')