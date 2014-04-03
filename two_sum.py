#!/usr/bin/env python

__author__ = "Rio"

def two_sum_naive(num, target):
    '''
    Given an array of integers, find two numbers such that they add up to a specific target number.

    Returns the indexes in decent order.

    Warning: this solution works fine but will fail in the time limitation as
    index() method in list is pretty slow, as the time complexity is O(n), which
    means the whole time complexity will become O(n^2)

    >>two_sum([2, 7, 11, 15], 9)
    >>(1, 2)
    '''
    content = {}

    for n in num:
        value = target - n
        if value in content:
            return (min(num.index(n)+1, content[value]+1), max(num.index(n)+1, content[value]+1))
        else:
            content[n] = num.index(n)

    return None

def two_sum(num, target):
    '''
    Replace index() method with num[i].
    '''
    content = {}

    for i in xrange(len(num)):
        n = num[i]
        value = target - n
        if value in content:
            a, b = i+1, content[value]+1
            return (min(a, b), max(a, b))
        else:
            content[n] = i

    return None

