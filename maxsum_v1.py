
# Name: Saw Lin Htet Oo
# ID: 6712114
# Sec: 542

import time


def max_sum(input):

    max_sum = float('-inf')

    for i in range(len(input)):
        for j in range(i, len(input)):
            curr_sum = 0
            for k in range(i, j + 1):
                curr_sum += input[k]
            if curr_sum > max_sum:
                max_sum = curr_sum
    return max_sum


start = time.process_time()
arr = list(map(int, input().split()))
print(max_sum(arr))
finish = time.process_time()
print("running time =", finish - start)
