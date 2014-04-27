#!/usr/bin/env python

__author__ = 'Rio'

class Solution:
    def combinations(self, num):
        """Produce all possible subsets and returns them as a list."""
        if not num:
            return []
        else:
            coms = self.combines(num)
            return self.construct(coms)

    def construct(self, combinations):
        """Construct a list from a iterable object"""
        return [value for value in combinations]

    def combines(self, num):
        if not num:
            yield []

        for i in range(len(num)):
            for comb in self.combines(num[i+1:]):
                yield comb+[num[i]]

def main():
    solution = Solution()
    print solution.combinations([1, 2, 3])

if __name__ == '__main__':
    main()    
