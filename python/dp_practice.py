# -*- coding: utf-8 -*-
#!/usr/bin/env python

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fib_cache(n):
    if n < 2:
        return 1

    cache = [-1 for value in range(n+1)]
    cache[0] = 1
    cache[1] = 1
    if cache[n] != -1:
        return cache[n]
    else:
        cache[n] = fib_cache(n-1) + fib_cache(n-2)
    return cache[n]

def find_fib(n):
    if n < 2:
        return 1
    cache = [-1 for value in xrange(n+1)]
    cache[0] = cache[1] = 1
    for i in xrange(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

class Coins:
    def __init__(self, coins):
        self.coins = coins
        self.result = []

    def coins(self, sum):
        for i in xrange(0, len(coins)):
            if sum == coins[i]:
                return 1
            if sum > coins[i]:
                
                
        
if __name__ == '__main__':
    #print fib(3)
    print fib_cache(3)
    print find_fib(3)
