import random
import math
r =1/ 2*math.pi
d = round(2 * r)
n = 10000
win = 0
for _ in range(n):
    ab = random.randint(1, 3)
    bc = random.randint(1, 3)
    ac = random.randint(1, 3)
    if(ab == 3 or bc == 3 or ac == 3):
        ...
    else:
        win += 1

prob = win/n
print(prob)

