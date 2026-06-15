
# Name: Saw Lin Htet Oo
# ID: 6712114
# Sec: 542

import time


def max_sum(arr):

    max_sum = float('-inf')

    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
    return max_sum


start = time.process_time()

arr = list(map(int, input().split()))
print(max_sum(arr))

finish = time.process_time()
print("running time =", finish - start)
