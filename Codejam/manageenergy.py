import sys

from sys import stdin, stdout
def readInts():
    return [int(x) for x in stdin.readline().split()]
def readInt():
    return int(stdin.readline())
def readLine():
    return stdin.readline().strip()

t = readInt()

for testcase in range(t):
    E, R, N = readInts()
    V = readInts()
    N = len(V)

    next_higher = [0] * N

    stack = []
    for i, a in enumerate(V):
        while stack and V[stack[-1]] < a:
            next_higher[stack.pop()] = i
        stack.append(i)

    eleft = E
    total = 0
    
    for i in range(N):
        next_high = next_higher[i]
        spend = 0
        if next_high == 0:
            spend = eleft
        else:
            incr = (next_high - i) * R
            gain = incr + eleft
            spend = max(min(gain - E, eleft), 0)
        total += spend * V[i]
        eleft = min(eleft + R - spend, E)

    print("Case #{}: {}".format(testcase+1, total))
    
    # maxind = V.index(max(V))

    # # def getval(A):
    # #     #print(A)
    # #     if len(A) == 0:
    # #         return 0

    # #     if len(A) == 1:
    # #         return A[0] * min(E, R)
        
    # #     mi = A.index(max(A))
    # #     #items = max(1, mi)
    # #     val = min(E, (mi+1) * R) * A[mi]
    # #     return val + getval(A[:mi]) + getval(A[mi+1:])

    # def getval(i, j, M, D):

    #     if i > j:
    #         return 0
        
    #     if i == j:
    #         if i == 0:
    #             return min(M, R) * V[i]
    #         else:
    #             if D == 'L':
    #                 return min(M, R) * V[i]
    #             else:
    #                 return min(E, R) * V[i]
        
    #     A = V[i: j+1]
    #     ind = A.index(max(A)) + i
        
    #     if D == 'L':
    #         if i == 0:
    #             val = min(E, (j-i) * R) * V[ind]
    #             return val + getval(0, ind - 1, min(E, ind * R), 'L') + getval(ind + 1, j, 0, 'R')
    #         else:
    #             val = min((ind - i) * R, M) * V[ind]
    #             return val + getval(i, ind - 1, min(E, (ind - i) * R), 'L') + getval(ind + 1, j, 0, 'R')
    #     if D == 'R':
    #         val = val = min((ind - i) * R, E) * V[ind]
    #         return val + getval(i, ind - 1, min(E, (ind - i) * R), 'L') + getval(ind + 1, j, 0, 'R')

    
    # res = V[maxind] * E + getval(0, maxind - 1, min(E, maxind * R), 'L') + getval(maxind + 1, N - 1, 0, 'R')