
import sys
sys.setrecursionlimit(10000)
 
count = 0
 
N,M = map(int,input().split())
w = list(map(int,input().split()))
v = list(map(int,input().split()))
 
x = [0] * N
 
def comb(i):
    global count
    count += 1
    if i == N:
        sw = sv = 0
        for j in range(N):
            if x[j] == 1:
                sw += w[j]
                sv += v[j]
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
      
print(comb(0))
print("Recursive counts:", count)
 