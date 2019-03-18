#https://www.acmicpc.net/problem/11170
a = int(input())
result = str()

for i in range(0,a):
    count = 0
    n, m = map(int, input().split())
    for t in range(n,m+1):
        b = str(t)
        for e in range(0,len(b)):
            if(b[e] == '0') :
                count = count + 1
    result = result + str(count) + '\n'

print(result[:-1])