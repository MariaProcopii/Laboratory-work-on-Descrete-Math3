import random

win = 0
money = 0
winNr = []
games = 10000
for _ in range(games):
    arr = []
    x = random.uniform(0, 1)
    for _ in range(10):
        a = random.uniform(0, 1)
        while(a in arr == True):
            a = random.uniform(0, 1)
        arr.append(a)
    for i in arr:
        if i > x:
            money += arr.index(i)
            win += 1
            winNr.append(i + 1)
            break;

prob = win/games
exmoney = money/games
# print(prob, exmoney)
k = (prob * exmoney)/(1 - prob)
print(k)


# setnr = set(winNr)
# dictionar = dict()
# for i in setnr:
#     dictionar[i] = winNr.count(i)
# all_values = dictionar.keys()
# maxValue = max(all_values)
# print(maxValue)


'''first versioin of code'''
# import random
# winarr = []
# for i in range(10000):
#     win = 0
#     x = random.uniform(0, 1)
#     n = random.uniform(0, 1)
#     while(n < x):
#         win += 1
#         n = random.uniform(0, 1)
#     winarr.append(win)
#
# a = set(winarr)
# expV = 0
# for i in a:
#     expV += i*winarr.count(i)/10000
# expV = round(expV)
# print(expV)
# probOfnumber = winarr.count(expV)/10000
# money = expV - 1
#
# k = (money*probOfnumber)/(1-probOfnumber)
# print(k)




