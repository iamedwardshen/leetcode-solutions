#!/usr/bin/env python

__author__ = 'Rio'

def subsets(num):
    """Generates all possible subsets and returns as a list."""
    if not num:
        return []
    else:
        subsets = combines(num)
        return construct(subsets)

def construct(subsets):
    return [value for value in subsets]

def combines(num, reverse=False):
    yield []
    for i in range(len(num)):
        for element in combines(num[i+1:]):
            if reverse:
                yield sorted(element+[num[i]])
            else:
                yield element+[num[i]]
