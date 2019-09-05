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
    s = str(N)
    l = len(s)

    b = ''
    for i in range(l):
        if s[i] == '4':
            b += '1' 
        else:
            b += '0'
    p1 = int(b)
    p2 = N-p1

    print("Case #" + str(testcase+1) + ": " + str(p1) + " " + str(p2))