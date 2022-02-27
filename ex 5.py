import random
l = 10
r = l/4
maxPoint = l - r
win = 0
for _ in range(10000):
    x = random.uniform(0, l)
    y = random.uniform(0, l)
    if (r <= x <= maxPoint and r <= y <= maxPoint):
        win += 1

prob = win/10000

print(prob)



# import random
# l = 10
# r = l/4
# maxPoint = l - r
# win = 0
# for _ in range(10000):
#     x = random.randint(0, l)
#     y = random.randint(0, l)
#     if (r <= x <= maxPoint and r <= y <= maxPoint):
#         win += 1
#
# prob = win/10000
#
# print(prob)
#the game is fair because the expected winning is equal to the amount we should pay