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

for testcase in range(t):
    S = readLine()

    res = S[0]
    
    for ch in S[1:]:
        if ch < res[0]:
            res += ch
        else:
            res = ch + res
    
    print("Case #{}: {}".format(testcase+1, res))