
n = int(input())

x = [0] * n

def comb(i):
    if i == n:
        print(*x)
        return
    
    x[i] = 0
    comb(i + 1)

    x[i] = 1
    comb(i + 1)

comb(0)
