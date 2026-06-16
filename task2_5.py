
n = int(input())

x = [0] * n


def comb(i):
    if i == n:
        print(*x)
        return 1
    
    total = 0
    for j in [0,1,2]:
        x[i] = j
        total += comb(i+1)
    return total

total = comb(0)
print(total)