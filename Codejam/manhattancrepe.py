import sys
from collections import defaultdict

from sys import stdin, stdout
def readInts():
    return [int(x) for x in stdin.readline().split()]
def readInt():
    return int(stdin.readline())
def readLine():
    return stdin.readline().strip()

t = readInt()

for testcase in range(t):
    p, q = readInts()

    n = defaultdict(int)
    s = defaultdict(int)
    w = defaultdict(int)
    e = defaultdict(int)

    for _ in range(p):
        x, y, d = readLine().split()
        if d == 'N':
            n[int(y)] += 1
        elif d == 'S':
            s[int(y)] += 1
        elif d == 'E':
            e[int(x)] += 1
        else:
            w[int(x)] += 1
    
    dpx = [0] * (q+1)
    dpy = [0] * (q+1)

    cnt = 0
    for i in range(q+1):
        dpx[i] += cnt
        if i in e:
            cnt += e[i]
    
    cnt = 0
    for i in range(q+1):
        dpy[i] += cnt
        if i in n:
            cnt += n[i]
    
    cnt = 0
    for i in range(q, -1, -1):
        dpx[i] += cnt
        if i in w:
            cnt += w[i]
    
    cnt = 0
    for i in range(q, -1, -1):
        dpy[i] += cnt
        if i in s:
            cnt += s[i]
    
    resx = dpx.index(max(dpx))
    resy = dpy.index(max(dpy))

    print("Case #{}: {} {}".format(testcase+1, resx, resy))

    