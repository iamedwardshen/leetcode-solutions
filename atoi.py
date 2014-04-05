#!/usr/bin/env python

__author__ = 'Rio'

def atoi(string):
    ''' atoi
    '''
    if not string: return string

    INT_MAX, INT_MIN = 2147483647, -2147483648

    # trim all whitespaces
    string = string.strip()

    flag = False
    index = 0
    if string[index] == '-':
        flag = True
        index += 1
    elif string[index] == '+':
        index += 1

    result = 0
    while index < len(string) and string[index] >= '0' and string[index] <= '9':
        result = result * 10 + int(string[index])
        index += 1

    if flag:
        result = -result

    if result > INT_MAX:
        return INT_MAX
    elif result < INT_MIN:
        return INT_MIN


    return result
