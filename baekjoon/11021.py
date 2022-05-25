# Problem 11021

count = int(input())

a_list = []
b_list = []
for i in range(count):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

for j in range(count):
    print(f'Case #{j+1}: {a_list[j] + b_list[j]}')    