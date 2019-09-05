import heapq
from functools import cmp_to_key

# Template start
from sys import stdin, stdout
def readInts():
    return [int(x) for x in stdin.readline().split()]
def readInt():
    return int(stdin.readline())
def readLine():
    return stdin.readline().strip()
def makecase(tc):
    return "Case #"+str(tc)+": "
# Template end

row, col = 0, 0
def neighbors(i, j):
    for nr, nc in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= nr < row and 0 <= nc < col:
            yield nr, nc


#Union find
parent = [0] * 5

def find(x):
    if parent[x] == 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    #print(rootX, rootY)
    if rootX == rootY:
        return False
    parent[rootX] = rootY
    return True