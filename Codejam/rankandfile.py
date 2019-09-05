from sys import stdin, stdout
from collections import defaultdict

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

for testcase in range(t):
    N = readInt()

    dct = defaultdict(int)

    for _ in range(2*N - 1):
        lst = readInts()

        for item in lst:
            dct[item] += 1

    res = []
    for key in dct:
        if dct[key] % 2 == 1:
            res.append(key)
    
    res = sorted(res)
    st = ' '.join(map(str, res))

    print("Case #{}: {}".format(testcase+1, st))