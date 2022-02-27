import random
import matplotlib.pyplot as plt
import  numpy as np

def game():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    sum = a + b + c
    return sum
win = 0
nr = 10000
for _ in range(nr):
    if(game() == 14):
        win += 1
prob14 = win/nr
for i in range(nr):
    probOfWinning = 1 - (1 - prob14) ** i
    if(probOfWinning > 0.47):
        print(i)
        break
y = []
for i in range(100):
    y.append(1 - (1 - prob14) ** i)
x = np.arange(100)

plt.plot(x, y)
plt.show()

