n, m = list(map(int, input().split()))

list1 = []
for i in range(n):
    list1.append(list(map(int, input().split())))

if m == 0 or n == 0:


list2 = list1
for i in range(n):
    for j in range(i, m):
        list1[i][j], list1[j][i] = list1[j][i], list1[i][j]

for i in list1:
    for j in range(len(i)):
        if j != len(i)-1:
            print(i[j], end=' ')
        else:
            print(i[j])
