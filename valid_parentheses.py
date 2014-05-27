#!/usr/bin/env python

__author__ = 'Rio'


def valid(s):
    """
    Solution: If a single element belongs to left parentheses,
    push it onto the stack, otherwise compare it with the top
    element in the stack. Finally, the stack should be empty.
    """
    if s is None:  # empty string is valid.
        return True

    stack = []
    for ele in s:
        if ele in '([{':
            stack.append(ele)
        else:
            if stack is not None and check_valid(ele, stack[-1]):
                stack.pop()
            else:
                return False

    return stack is None


def check_valid(c1, c2):
    return (c1 == '(' and c2 == ')'
            or c1 == '[' and c2 == ']'
            or c1 == '{' and c2 == '}')