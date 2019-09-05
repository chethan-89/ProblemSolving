import sys
from collections import defaultdict

from sys import stdin, stdout


def readInts():
    return [int(x) for x in stdin.readline().split()]


def readInt():
    return int(stdin.readline())


def readLine():
    return stdin.readline().strip()


t = readInt()

for testcase in range(t):
    r, c = readInts()
    mat = []
    for _ in range(r):
        mat.append(readLine().split())

    def issolnpossible(arr):
        b = False

        for i in range(row):
            for j in range(col):
