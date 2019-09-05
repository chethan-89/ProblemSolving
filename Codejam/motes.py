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
    A, N = readInts()
    arr = readInts()
    arr = sorted(arr)

    dp = {}

    def getsoln(i, j, mote):
        #print(i, j, mote)
        if i > j:
            return 0
        
        if i == j:
            if mote > arr[i]:
                return 0
            else:
                return 1

        if (i, j, mote) in dp:
            return dp[(i, j, mote)]

        start = mote

        for k in range(i, j+1):
            if arr[k] < start:
                start += arr[k]
            else:
                break
        
        if start > arr[k]:
            return 0
        
        ans = 0
        if start > 1:
            ans = 1 + min(getsoln(k, j, start + start - 1), getsoln(k, j-1, start))
        else:
            ans = 1 + getsoln(k, j-1, start)
        
        dp[(i, j, mote)] = ans
        return ans
    
    res = getsoln(0, N - 1, A)

    print("Case #{}: {}".format(testcase+1, res))
