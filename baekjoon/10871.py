# Problem 10871

import sys


max_num, compare_num = map(int, sys.stdin.readline().rstrip().split())

input_num = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(max_num):
    if input_num[i]< max_num:
        print(input_num[i], end=' ')


