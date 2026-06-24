
# Name: Saw Lin Htet Oo
# ID: 6712114
# Section: 542

import sys
import time

sys.setrecursionlimit(10000)

c = list(map(int, input().split()))
n = int(input())
min_coin = [0] * (n+1)

count = 0

start = time.process_time()

def coinChange(n , c):
    global count, min_coin
    count += 1

    if min_coin[n] != 0:
        return min_coin[n]

    if n == 0:
        return 0
    
    v = float('inf')

    for coin in c:
        if coin <= n:
            v = min(coinChange(n-coin, c)+1,v)
    min_coin[n] = v
    return v

result = coinChange(n,c)
finish = time.process_time()

print('recursion count: ' , count)
print('Answer: ', result)
print('Total Time: ', finish - start)