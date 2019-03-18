#https://www.acmicpc.net/problem/5800
a = int(input())
c = ''

for i in range(1, a + 1):
    lgg = 0
    d = input().split()
    e = int(d[0])
    del d[0]
    b = []
    for t in range(0, e):
        b.append(int(d[t]))
    b.sort()
    for m in range(1, e):
        f = b[m] - b[m - 1]
        if(lgg < f):
            lgg = b[m] - b[m - 1]
    c = c + 'Class ' + str(i) + '\n'
    c = c + 'Max ' + str(b[-1])
    c = c + ', Min ' + str(b[0]) + ', Largest gap ' + str(lgg) + '\n'
    
print(c)
