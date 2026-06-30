
# Name: Saw Lin Htet Oo
# ID: 6712114
# Sec: 542

import sys,time

sys.setrecursionlimit(1000000)

P = list(map(int,input().split()))
l = len(P)
recursive_call = 0

minCoin = [None] * (l+1)

def maxRevenue(l,p):
    global recursive_call
    recursive_call+=1

    if minCoin[l] is not None:
        return minCoin[l]
    
    if l == 0:
        return 0
    
    v = float('-inf')

    for c in range(l):
        v = max(maxRevenue(l-(c+1),p)+p[c],v)
        minCoin[l] = v
    return v

st = time.process_time()
print(maxRevenue(l,P))
print("Recursive_Call: ",recursive_call)
et = time.process_time()

print("Time: ",et-st)
