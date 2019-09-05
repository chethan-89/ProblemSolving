import sys
import math

from sys import stdin, stdout
def readInts():
    return [int(x) for x in stdin.readline().split()]
def readInt():
    return int(stdin.readline())
def readLine():
    return stdin.readline().strip()

t = readInt()

for testcase in range(t):
    r, t = readInts()

    # cnt = 0
    # spent = 0
    # currsize = r * r
    # currradius = r

    # while spent <= t:
    #     cnt += 1
    #     currradius += 1
    #     nextsize = currradius * currradius
    #     spent += nextsize - currsize
    #     currradius += 1
    #     currsize = currradius * currradius
    
    # print(cnt, spent)

    # b = 2*r - 1
    # a = 2
    # c = -t
    # sqr = math.sqrt((b*b) - (4*a*c))
    # n = math.floor((-b + sqr)/(2*a))

    def gettotalarea(n):
        return (2*n*n) + (2*r*n) - n

    # n = n + 10
    # while gettotalarea() > t:
    #     n -= 1
    
    # print("Case #{}: {}".format(testcase+1, n))

    # l = 1
    # r = t

    def getsoln(l, r):
        if l > r:
            return r
        
        mid = (l + r) // 2

        area = gettotalarea(mid)

        if area <= t:
            return getsoln(mid+1, r)
        else:
            return getsoln(l, mid-1)
    
    res = getsoln(1, t)
    print("Case #{}: {}".format(testcase+1, res))

        

