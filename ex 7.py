import random

win = 0
nrofmembers = 10
for _ in range(10000):
    arr1 = []
    arr2 = []
    for i in range(nrofmembers):
        a = random.randint(1, nrofmembers)
        while a in arr1:
            a = random.randint(1, nrofmembers)
        arr1.append(a)
    for j in range(nrofmembers):
        b = random.randint(1, nrofmembers)
        while b in arr2:
            b = random.randint(1, nrofmembers)
        arr2.append(b)
    if arr1 == arr2:
        win += 1

print(win)





















#
# win = 0
# n = int(10/2)
# for _ in range(1):
#     arrA = []
#     arrB = []
#     for _ in range(2):
#         for i in range(n):
#             a = random.randint(1, 10)
#             b = random.randint(1, 10)
#             while (a == b):
#                 a = random.randint(1, 10)
#             if(len(arrA) == 10):
#                 while((arrA[i] == arrA[i + n] and arrB[i] == arrB[i + n])
#                         or (arrA[i] == arrB[i] and arrA[i + n] == arrB[i + n])
#                         or (arrA[i] == arrB[i + n] and arrB[i] == arrA[i + n])
#                         or arrA[i] == arrB[i] or arrA[i + n] == arrB[i + n]):
#                     a == random.randint(1, 10)
#                     win += 1
#
#             arrA.append(a)
#             arrB.append(b)
#     print(arrB)
#     print(arrA)
#
# prob = win/10000
# print(prob)


