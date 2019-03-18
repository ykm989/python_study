#https://www.acmicpc.net/problem/11365

a = input()
while('END' != a):
    i = 0
    for i in range(0,len(a)):
        print(a[-(i + 1)] , end = '')
        i = i + 1
    print()
    a = input()
