#https://www.acmicpc.net/problem/2506
n = int(input())
ads = -1
total = 0
a = input().split()

for i in range(0, n):
    if(int(a[i]) == 1):
        ads = ads + 1
        total = total + 1 + ads
    else:
        ads = -1
print('%d' %total)
