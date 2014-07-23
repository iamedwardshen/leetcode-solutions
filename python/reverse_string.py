#!/usr/bin/env python

def reverse_word(s):
    s = s.strip().split()
    return ' '.join(reversed(s))

def reverse_word_2(s):
    s = s.strip().split()
    return s[::-1]
