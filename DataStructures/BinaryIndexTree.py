
nums = [3, 4, 5, 7]
n = len(nums)
tree = [0] * (n+1)


def getsum(i):
    i = i + 1

    total = 0
    while i > 0:
        total += tree[i]
        i -= (i & -i)

    return total


def update(i, val):

    i = i + 1
    while i <= n:
        tree[i] += val
        i += (i & -i)


def rangeupdate(l, r, val):
    update(l, val)
    update(r+1, -val)


def rangesum(l, r):
    return getsum(r) - getsum(l-1)


for i, val in enumerate(nums):
    update(i, val)

print(tree)
print(getsum(2), getsum(3))

update(1, 3)
print(getsum(2), getsum(3))
print(rangesum(2, 3))

rangeupdate(1, 2, 2)
print(getsum(2), getsum(3))
