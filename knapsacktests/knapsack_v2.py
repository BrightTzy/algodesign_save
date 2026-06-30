

# Name: Saw Lin Htet Oo
# ID: 6712114
# Sec: 542

import sys
import time
sys.setrecursionlimit(10000)

recursion_count = 0
N,M = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))


def maxVal(i, C):
    global recursion_count
    recursion_count += 1

    if i == N:
        return 0
    else:
        skip = maxVal(i+1,C)
        if W[i] <= C:
            take = V[i] + maxVal(i+1, C-W[i])
        else:
            take = -1
        return max(skip, take)

start = time.process_time()
print("Ans: ",maxVal(0, M))
print("recursion_count: ", recursion_count)
end = time.process_time()
print("Run Time: ", end - start)