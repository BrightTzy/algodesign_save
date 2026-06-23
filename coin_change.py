

import sys
import time

c = list(map(int, input().split()))
n = int(input())

count = 0

start = time.process_time()

def coinChange(n , c):
    global count
    count += 1
    if n == 0:
        return 0
    
    v = float('inf')

    for coin in c:
        if coin <= n:
            v = min(coinChange(n-coin, c)+1,v)
    return v

result = coinChange(n,c)
finish = time.process_time()

print(count)
print(result)
print('Total Time: ', finish - start)
