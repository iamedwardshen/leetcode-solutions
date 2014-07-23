#!/usr/bin/env python

__author__ = 'Rio'

def eval_rpn(tokens):
    '''
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    >> eval_rpn(["2", "1", "+", "3", "*"])
    >> 9
    >> eval_rpn(["4", "13", "5", "/", "+"])
    >> 6
    '''
    OPS = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: y-x,
        '*': lambda x, y: x*y,
        '/': lambda x, y: y/x
        }

    stack = []

    for token in tokens:
        if token in OPS:
            stack.append(int(OPS[token](stack.pop(), stack.pop())))
        else:
            stack.append(int(token))

    return stack.pop()
