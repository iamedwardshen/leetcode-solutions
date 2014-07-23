#!/usr/bin/env python

__author__ = 'Rio'

book = {
    '1': '',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    '0': ''
}

def letterCombinations(digits):
    if not digits:
        return []

    letters = ''.join([v for k, v in book])
    combinations = combines(letters)
    return construct(combinations)

def combines(digits):
    
