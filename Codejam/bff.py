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
    lst = readInts()

    def getcount(n):
        visited = set()

        total = 0
        curr = n
        
        while curr not in visited:
            total += 1
            visited.add(curr)
            curr = lst[curr-1]

        if lst[curr-1] == n or lst[curr-1] == lst[n-1]:
            return total
        else:
            return 0 

    res = 0
    for n in range(1, N+1):
        cnt = getcount(n)  
        if cnt > res:
            res = cnt
    
    print("Case #{}: {}".format(testcase+1, res))