import sys

from sys import stdin, stdout
def readInts():
    return [int(x) for x in stdin.readline().split()]
def readInt():
    return int(stdin.readline())
def readLine():
    return stdin.readline().strip()


t = readInt()

for testcase in range(t):

    size = readInts()

    row = size[0]
    col = size[1]

    if row == 1 and col == 1:
        print("Case #" + str(testcase+1) + ": " + "POSSIBLE")
        print("1 1")
    elif (row <= 3 and col <= 3) or row == 1 or col == 1:
        print("Case #" + str(testcase+1) + ": " + "IMPOSSIBLE")
    else:
        print("Case #" + str(testcase+1) + ": " + "POSSIBLE")

        def printindexes(r, c):
            for i in range(1, r+1, 2):
                for j in range(2, c+1, 2):
                    print(str(i) + ' ' + str(j))
            for i in range(2, r+1, 2):
                for j in range(1, c+1, 2):
                    print(str(i) + ' ' + str(j))
        
        if col <= 3:
            printindexes(col, row)
        else:
            printindexes(row, col)

