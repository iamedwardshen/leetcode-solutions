#!/usr/bin/env python

__author__ = 'Rio'

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        if not intervals or len(intervals) <= 1:
            return intervals

        intervals.sort(lambda x, y: x.start-y.start)

        results = []
        length = len(intervals)
        last = intervals[0]
        for i in range(1, length):
            curr = intervals[i]
            if curr.start <= last.end:
                last.end = max(last.end, current.start)
            else:
                results.append(last)
                last = curr

        return results

if __name__ == '__main__':
    a = Interval(1, 3)
    intervals = []
    intervals.append(a)
    s = Solution()
    results = s.merge(intervals)
    for ele in results:
        print ele.start
