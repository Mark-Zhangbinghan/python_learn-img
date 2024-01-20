n = int(input())  # 录入行数
a = []  # 建立空列表
for i in range(n):
    a.append(list(map(int, input().split())))  # 利用append方法逐行录入列表a
x, y = list(map(int, (input().split())))

p = len(a)
while p > 0:
    if a[p - 1][0] <= x <= a[p - 1][0] + a[p - 1][2] and a[p - 1][1] <= y <= a[p - 1][1] + a[p - 1][3]:
        print(p)
        break
    else:
        p -= 1
else:
    print(-1)
