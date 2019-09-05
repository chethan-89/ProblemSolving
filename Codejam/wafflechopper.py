t = int(input())

def getcookiecnt(mat, r1, c1, r2, c2):
    #print("here",r1,c1,r2,c2)
    cookie = 0
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            cookie += mat[i][j]
    #print("cookie", cookie)
    return cookie

for testcase in range(t):
    data = [int(x) for x in input().split()]

    R = data[0]
    C = data[1]
    H = data[2]
    V = data[3]

    totalcookie = 0
    rowmat = [0] * R
    colmat = [0] * C

    mat = [[0]*C for _ in range(R) ]

    for row in range(R):
        d = list(input())
        rowmat[row] = d.count('@')
        totalcookie += rowmat[row]
        for col in range(C):
            if d[col] == '@':
                colmat[col] += 1
                mat[row][col] = 1

    if totalcookie == 0:
        print("Case #" + str(testcase+1) + ": POSSIBLE")
        continue

    if totalcookie % ((H + 1) * (V + 1)) != 0:
        print("Case #" + str(testcase+1) + ": IMPOSSIBLE")
        continue
    
    cookiecnt = totalcookie/((H + 1) * (V + 1))

    hc = totalcookie/(H + 1)
    hs = H + 1
    curr = 0
    hcut = []
    for row in range(R):
        curr += rowmat[row]
        if curr == hc:
            curr = 0
            hs -= 1
            hcut.append(row)
            continue
        if curr > hc:
            break
    
    if hs != 0:
        print("Case #" + str(testcase+1) + ": IMPOSSIBLE")
        continue
    
    def verticalvalidation():
        vc = totalcookie/(V + 1)
        vs = V + 1
        curr = 0
        vcstart = -1
        for col in range(C):
            curr += colmat[col]
            if curr == vc:
                hcstart = -1
                for k in hcut:
                    cookie = getcookiecnt(mat, hcstart+1, vcstart+1, k, col)
                    if cookie != cookiecnt:
                        return False
                    hcstart = k
                vcstart = col
                curr = 0
                vs -= 1
            if curr > vc:
                return False

        if vs != 0:
            return False
        else:
            return True

    val = verticalvalidation()
    if val:
        print("Case #" + str(testcase+1) + ": POSSIBLE")
    else:
        print("Case #" + str(testcase+1) + ": IMPOSSIBLE")
    