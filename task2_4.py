

n = int(input())
k = int(input())

x = [0] * n

def comb(i):
    total = 0
    if i == n:
        if sum(x) == k:
            total += 1
            print(*x)
        return total
    
    for j in [0,1]:
        x[i] = j
        total += comb(i+1)
    return total

total = comb(0)
print(total)