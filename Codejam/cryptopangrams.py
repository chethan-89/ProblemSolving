import heapq
from itertools import chain, count

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

def getlargestfactor(n):
    for f in chain([2], count(3, 2)):
        while n % f == 0:
            n //= f
            if f >= n ** 0.5:
                return f if n == 1 else n

for testcase in range(t):

    data = readInts()
    N = data[0]
    L = data[1]

    lst = readInts()
    factors = []
    primesdct = set()

    def getprimefactors(num):
        for prime in primesdct:
            if num % prime == 0:
                return (prime, num // prime)
        
        fct = getlargestfactor(num)
        return (fct, num // fct)
        

    for i in range(L):
        (p1, p2) = getprimefactors(lst[i])
        primesdct.add(p1)
        primesdct.add(p2)
        factors.append((p1, p2))
    
    primes = sorted(primesdct)
    alphabet = {}

    for i in range(26):
        alphabet[primes[i]] = chr(i + 65)

    res = ""
    for i in range(L-1):
        if factors[i][0] not in factors[i+1]:
            res += alphabet[factors[i][0]]
        elif factors[i][1] not in factors[i+1]:
            res += alphabet[factors[i][1]]
        else:
            if i < L-2:
                if factors[i][0] not in factors[i+2]:
                    res += alphabet[factors[i][0]]
                else:
                    res += alphabet[factors[i][1]]
            else:
                res += alphabet[factors[i][0]]

    
    if factors[L-1][0] in factors[L-2]:
        res += alphabet[factors[L-1][0]]
        res += alphabet[factors[L-1][1]]
    else:
        res += alphabet[factors[L-1][1]]
        res += alphabet[factors[L-1][0]]

    print("Case #" + str(testcase+1) + ": " + res)