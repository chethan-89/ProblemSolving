import math

t = int(input())

for testcase in range(t):
    A = float(input())
    srtfn = math.sqrt(6 - 2*A*A)

    x1 = (3 + A + srtfn)/12
    y1 = (-2*A + srtfn)/12
    z1 = (3 - A - srtfn)/12

    x2 = (2*A -srtfn)/12
    y2 = (A + srtfn)/6
    z2 = y1

    x3 = z1
    y3 = x2
    z3 = x1

    print("Case #" + str(testcase + 1) + ":")
    print(x1,y1,z1)
    print(x2,y2,z2)
    print(x3,y3,z3)
