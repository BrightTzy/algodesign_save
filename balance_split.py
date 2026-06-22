
# Name: Saw Lin Htet Oo
# ID: 6712114
# Section: 542


n = list(map(int, input().split()))

curr_diff = 0
min_diff = float('inf')
x = [0] * len(n)


def balance_split(i):
    global min_diff

    if i == len(n):
        left = []
        right = []

        for k in range(len(n)):
            if x[k] == 1:
                right.append(n[k])
            else:
                left.append(n[k])
        curr_diff = abs(sum(left) - sum(right))

        if curr_diff < min_diff:
            min_diff = curr_diff
        return
    
    for j in [0,1]:
        x[i] = j
        balance_split(i+1)
    return

balance_split(0)
print(min_diff)
