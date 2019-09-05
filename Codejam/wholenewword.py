
t = int(input())

for testcase in range(t):

    data = input().split()
    N = int(data[0])
    L = int(data[1])

    wordset = set()
    llist = [set() for _ in range(L)]

    for _ in range(N):
        word = input()
        wordset.add(word)

        for i in range(L):
            llist[i].add(word[i])

    def getnewword():

        for word in wordset:
            for i in range(L):
                lst = llist[i]
                for ch in lst:
                    tmpword = word[:i] + ch + word[i+1:]
                    if tmpword not in wordset:
                        return tmpword
        
        return "-"

    res = getnewword()
    print("Case #" + str(testcase+1) + ": " + res)
    