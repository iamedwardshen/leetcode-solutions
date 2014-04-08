#!/usr/bin/env python

def valid_palidrome(s):
    if not s: return True

    s = s.lower()

    content = []
    for element in s:
        if '0' <= element <=  '9' or 'a' <= element <= 'z':
            content.append(element)

    return content == content[::-1]
