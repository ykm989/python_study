#https://www.acmicpc.net/problem/10162 최소
import sys

t = int(input())
a = 0
b = 0
c = 0
if(t < 1 or t > 10000):
    sys.exit()
    
while(t >= 300):
    t = t - 300
    a = a + 1
while(t >= 60):
    t = t - 60
    b = b + 1
while(t >= 10):
    t = t - 10
    c = c + 1
if((a == 0 and b == 0 and c == 0) or t > 0):
    print('-1')
else:
    print('%d %d %d' %(a, b, c))
