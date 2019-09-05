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
    A = readInt()

    C = []

    for _ in range(A):
        C.append(readLine())
    
    ind = 0
    res = ''

    def getwinnerletter(lst):
        lst = sorted(lst)
        st = ''.join(lst)
        if st == 'R':
            return 'P'
        elif st == 'P':
            return 'S'
        elif st == 'S':
            return 'R'
        elif st == 'PR':
            return 'P'
        elif st == 'RS':
            return 'R'
        elif st == 'PS':
            return 'S'
        
        return ''
    
    def keepitem(ch1, ch2):
        if ch1 == 'R' and ch2 == 'S':
            return False
        elif ch1 == 'S' and ch2 == 'P':
            return False
        elif ch1 == 'P' and ch2 == 'R':
            return False
        
        return True

    def issolnpossible():

        global res, C, ind

        while len(C) > 0:
            s = set()
            for item in C:
                tind = ind
                l = len(item)
                if l <= ind:
                    tind = ind % l
                s.add(item[tind])
            
            if len(s) == 3:
                return False
            
            ch = getwinnerletter(list(s))

            if ch == '':
                return False

            res += ch

            if len(s) == 1:
                return True
            
            tmp = []
            for item1 in C:
                t = ind
                l = len(item1)
                if l <= ind:
                    t = ind % l
                if keepitem(ch, item1[t]):
                    tmp.append(item1)
            C = tmp
            ind += 1
        return True

    ret = issolnpossible()

    if ret:
        print("Case #{}: {}".format(testcase+1, res))
    else:
        print("Case #{}: IMPOSSIBLE".format(testcase+1))
    


