import random
import math

n = 10000
winA = 0
winB = 0
for _ in range(n):
    b = random.randint(-1, 1)
    c = random.randint(-1, 1)
    if(b**2 - 4*c >=0):
        winA += 1
    if(b**2 - 4*c >=0 and b<=0 and c<=0):
        winB += 1

prob1 = winA/n
prob2 = winB/n
print(f"a)P = {prob1}\nb)P = {prob2}")
