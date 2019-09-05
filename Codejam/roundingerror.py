import heapq

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

    data = readInts()
    N = data[0]
    L = data[1]

    classes = readInts()

    lst = []

    singleratio = 100 / N

    tillnow = 0
    for ns in classes:
        val = ns * 100 / N
        tillnow += ns
        heapq.heappush(lst, (-val, ns))

    #print(lst)
    for i in range((N-tillnow)):
        topitem = lst[0][1]
        topper = (topitem + 1) * 100 / N
        #print(topper)
        if int(topper) < round(topper):
            heapq.heappop(lst)
            heapq.heappush(lst, (-topper, topitem+1))
        else:
            heapq.heappush(lst, (-singleratio, 1))
    #print(lst)

    res = 0
    for item in lst:
        res += int(round(-item[0]))
    
    print("Case #" + str(testcase+1) + ": " + str(res))