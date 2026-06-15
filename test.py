
n = [10, 31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

curr_sum = 0
max_sum = 0

for i in range(len(n)):
    curr_element = n[i]
    curr_sum += curr_element
    if curr_sum > max_sum:
        max_sum = curr_sum
    if curr_sum < 0:
        curr_sum = 0
print(max_sum)
