# Problem 15552
import sys

count = int(sys.stdin.readline().rstrip()) # input 대신 sys.stdin.readline 사용 rstrip은 계행 제거용.

a_list=[]
b_list=[]
for i in range(count):
    a, b = map(int, sys.stdin.readline().split())

    a_list.append(a)
    b_list.append(b)

for j in range(count):
    print(a_list[j]+b_list[j])