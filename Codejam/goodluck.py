import sys

from sys import stdin, stdout
def readInts():
    return [int(x) for x in stdin.readline().split()]
def readInt():
    return int(stdin.readline())
def readLine():
    return stdin.readline().strip()

t = readInt()

for _ in range(t):
    R, N, M, K = readInts()

    print("Case #1:")

    for testset in range(R):
        pdts = readInts()

        lst = []
        
        for i in range(2, M+1):
            for j in range(2, M+1):
                for k in range(2, M+1):
                    lst.append([i,j,k])

        def issoln(item):
            subsets = [1]
            subsets.append(item[2])
            subsets.append(item[1])
            subsets.append(item[0])
            subsets.append(item[2] * item[0])
            subsets.append(item[1] * item[0])
            subsets.append(item[2] * item[1])
            subsets.append(item[2] * item[1] * item[0])

            for pdt in pdts:
                if pdt not in subsets:
                    return False
            
            return True

        for item in lst:
            if issoln(item):
                print("{}{}{}".format(item[0],item[1],item[2]))
                break
            
            
            