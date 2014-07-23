#!/usr/bin/env python

__author__ = 'Rio'

def permutes(num):
    if not num:
        return []
    else:
        permutations = permutation(num)
        return construct(permutations)

def construct(permutations):
    return [value for value in permutations]

def permutation(num):
    if not num:
        yield []
    for i in range(len(num)):
        for element in permutation(num[:i]+num[i+1:]):
            yield [num[i]]+element

if __name__ == '__main__':
    print permutes([1, 2, 2])
