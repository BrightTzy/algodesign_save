
n = int(input())

x = [0] * n

def comb(i):
    if i == n:
        print(*x)
        return
    
    for j in [0,1]:
        x[i] = j
        comb(i+1)

comb(0)
