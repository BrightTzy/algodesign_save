
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

x = [0] * N

def comb(i):
    global recursion_count
    recursion_count += 1

    if i == N:
        sw = sv = 0
        for j in range(N):
            if x[j] == 1:
                sw += W[j]
                sv += V[j]
        if sw > M:
            return -1
        else:
            return sv
    else:
        x[i] = 0
        a = comb(i+1)
        x[i] = 1
        b = comb(i+1)
        return max(a,b)


start = time.process_time()
print("Ans: ", comb(0))
print("recursion_count: ", recursion_count)
end = time.process_time()
print("Run Time: ", end - start)
    