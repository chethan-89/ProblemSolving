import math
import sys

from sys import stdin, stdout
def readInts():
    return [int(x) for x in stdin.readline().split()]
def readInt():
    return int(stdin.readline())
def readLine():
    return stdin.readline().strip()
def makecase(tc):
    return "Case #"+str(tc)+": "
#template end

t = readInt()

def getdiagonal(a, b):
    return math.sqrt(a*a + b*b)

for testcase in range(t):
    data = readInts()
    N = data[0]
    P = data[1]

    cookies = []
    totalperimeter = 0
    for i in range(N):
        cookie = readInts()
        cookies.append(
            (
                min(cookie[0], cookie[1]), 
                getdiagonal(cookie[0], cookie[1])
            )
        )
        totalperimeter += 2 * (cookie[0] + cookie[1])
    
    diff = P - totalperimeter

    dct = {}

    def recurfun(total, minval, maxval):

        if minval > diff:
            return sys.maxsize

        if maxval >= diff and minval <= diff:
            return 0
        
        if total >= N:
            return diff - maxval
        
        if (total, minval) in dct:
            return dct[(total, minval)]

        r1 = recurfun(total+1, minval, maxval)
        r2 = recurfun(total+1, minval+2*cookies[total][0], maxval+2*cookies[total][1])
        val = min(r1, r2)
        dct[(total, minval)] = val
        return val
    
    mindist = recurfun(0, 0, 0)
    result = "%.6f" % (P - mindist)
    print("Case #" + str(testcase+1) + ": " + result)
