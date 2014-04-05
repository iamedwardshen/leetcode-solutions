#!/usr/bin/env python

__author__ = "Rio"

def reverse_integer(x):
    ''' Reverse digits of an integer
    '''

    # Leetcode doesn't support 'import' statement, define two constants locally
    MAX_INTEGER = 9223372036854775807
    MIN_INTEGER = -MAX_INTEGER

    flag = False
    if x < 0:
        flag = True
        x = abs(x)

    result = 0
    while x:
        result = result*10 + x%10
        x = x / 10

    if flag: result = -result

    if result > MAX_INTEGER:
        return MAX_INTEGER
    elif result < MIN_INTEGER:
        return MIN_INTEGER

    return result
