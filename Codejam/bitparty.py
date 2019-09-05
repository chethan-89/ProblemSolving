t = int(input())

for testcase in range(t):
    data = [int(X) for X in input().split()]
    R = data[0]
    B = data[1]
    C = data[2]

    CA = []

    for i in range(C):
        data1 = [int(X) for X in input().split()]
        CA.append((data1[0], data1[1], data1[2]))
    
    def issolutionpossible(m):
        arr = []
        for item in CA:
            if m - item[2] > 0:
                d = (m - item[2])//item[1]
                arr.append(min(item[0], d))
            else:
                arr.append(0)
        
        arr.sort(reverse=True)
        s = sum(arr[:R])
        if s >= B:
            return True
        else:
            return False

    low = 0
    high = int(1e18 + 1e9 + 1)
    print(high)
    def findminval(l, h):

        if l > h:
            return l

        mid = (l+h)//2

        ret = issolutionpossible(mid)
        
        if ret:
            return findminval(l, mid - 1)
        else:
            return findminval(mid + 1, h)


    res = findminval(low, high)

    print("Case #" + str(testcase+1) + ": " + str(res))
