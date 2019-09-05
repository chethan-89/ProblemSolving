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

    N = readInt()
    S = readLine()

    res = ''

    for ch in S:
        res += 'E' if ch == 'S' else 'S'

    print("Case #" + str(testcase+1) + ": " + res)