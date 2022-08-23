# https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=false

def getMoneySpent(keyboards, drives, b):
    ls = []
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            print(keyboards[i], drives[j])
            summ = keyboards[i] + drives[j]    
            
            if summ <= b:
                ls.append(summ)
            else:
                ls.append(-1)
    return max(ls)
