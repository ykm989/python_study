#https://www.acmicpc.net/problem/2675
t = int(input())
p = str()

for i in range(0,t):
    o = input().split()
    r = int(o[0])
    s = o[1]
    for a in range(0, len(s)):
        for b in range(0, r):
            p = p + s[a]
    p = p + '\n'
print('%s' %p)
