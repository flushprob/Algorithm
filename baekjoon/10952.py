# Problem 10952

import sys


a_list=[]
b_list=[]
while(1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a == 0 & b == 0:
        break
    else:
        a_list.append(a)
        b_list.append(b)

# print(a_list, b_list)

for i in range(len(a_list)):
    print(a_list[i]+b_list[i])