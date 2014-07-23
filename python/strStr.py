#!/usr/bin/env python

__author__ = 'Rio'

def strStr(haystack, needle):
    index = haystack.find(needle)
    if index == -1:
        return None
    return haystack[index:]
