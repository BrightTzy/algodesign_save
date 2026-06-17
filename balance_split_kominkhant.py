import sys
sys.setrecursionlimit(10000)

y = [5,8,13,27,14]
x = [None]*len(y)
difference = float('inf')
GroupA = []
GroupB = []
def balance_Split(i):
    global difference, GroupA, GroupB
    group_1 = []
    group_2 = []
    if i == len(y):
        for k in range(len(y)):
            if x[k] == 0:
                group_1.append(y[k])
            else:
                group_2.append(y[k])
        temp = abs(sum(group_1)- sum(group_2))
        if temp < difference:
            difference = temp
            GroupA = group_1
            GroupB = group_2
        return 
    for j in range(0,2):
        x[i] = j
        balance_Split(i+1)
    
balance_Split(0)
print('group 1=',GroupA)
print('group 2=',GroupB)
print('minimum difference=',difference)