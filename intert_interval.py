#!/usr/bin/env python

__author__ = 'Rio'

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]

        intervals.append(newInterval)
        intervals.sort(lambda x, y: x.start-y.start)

        result = []
        length = len(intervals)
        last = intervals[0]
        for i in range(1, length):
            current = interval[i]
            if current.start <= last.end:
                last.end = max(current.end, last.end)
            else:
                result.append(last)
                last = current

        result.append(last)


        return result
