
# Name: Saw Lin Htet Oo
# ID: 6712114
# Sec: 542

n = int(input())

curr_sum = 0
max_sum = 0

for i in range(n):
    curr_element = int(input())
    curr_sum += curr_element
    if curr_sum > max_sum:
        max_sum = curr_sum
    if curr_sum < 0:
        curr_sum = 0
print(max_sum)
