from sys import stdin, stdout
from collections import defaultdict

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
    S = readLine()
    dct = defaultdict(int)
    lst = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    
    def getsoln(i, s, res):

        #print(i, s, res)

        if len(s) == 0:
            return res

        if i >= len(lst):
            return ''
        
        tmp2 = s
        possible = False
        while True:
            tmp = tmp2
            cnt = 0
            for ch in lst[i]:
                ind = tmp.find(ch)
                if ind > -1:
                    tmp = tmp[:ind] + tmp[ind+1:]
                    cnt += 1
                else:
                    break
            #print(cnt, tmp)
            if cnt == len(lst[i]):
                possible = True
                tmp2 = tmp
                res += str(i)
            else:
                break
        
        #print(s, tmp2)
        if possible:
            return getsoln(i+1, tmp2, res)
        else:
            return getsoln(i+1, s, res)
        
    
    out = ''
    for i in range(1):
        ret = getsoln(i, S, '')
        if len(ret) > 0:
            out = ret
            break
    
    print("Case #{}: {}".format(testcase+1, out))