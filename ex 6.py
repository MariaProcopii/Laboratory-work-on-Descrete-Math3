import  random
import matplotlib.pyplot as plt

y = []
for _ in range(10000):
    win = 0
    for _ in range(100):
        a = random.randint(0, 1)
        if(a == 1):
            win += 1
    y.append(win)

unique = list(set(y))
elem = []

for i in unique:
    elem.append(y.count(i))

plt.bar(unique, elem, color = ["teal"])
# plt.xlim(35, 65)
# plt.ylim(0, 100)
plt.show()

# import  random
# import matplotlib.pyplot as plt
#
# x = []
# for i in range(1000):
#    x.append(i)
# y = []
#
# for _ in range(1000):
#     win = 0
#     for _ in range(100):
#         a = random.randint(0, 1)
#         if(a == 1):
#             win += 1
#     y.append(win)
#
# plt.bar(x, y)
# plt.show()



