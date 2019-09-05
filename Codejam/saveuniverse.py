t = int(input())

def getSCount(pr):
    count = 0
    for ch in pr:
        if ch == 'S':
            count += 1
    return count

def getDamage(pr):
    power = 1
    damage = 0
    for ch in pr:
        if ch == 'S':
            damage += power
        if ch == 'C':
            power *= 2
    return damage

for testcase in range(t):
    case = input().split()
    d = int(case[0])
    pr = list(case[1])
    attempt = 0
    
    scount = getSCount(pr)
    if scount > d:
        print("Case #" + str(testcase+1) + ": IMPOSSIBLE")
        continue
    
    currdamage = getDamage(pr)
    while currdamage > d:
        for i in range(len(pr) - 2, -1, -1):
            if pr[i] == 'C' and pr[i+1] == 'S':
                pr[i] = 'S'
                pr[i+1] = 'C'
                currdamage = getDamage(pr)
                attempt += 1
                break
    
    print("Case #" + str(testcase+1) + ": " + str(attempt))