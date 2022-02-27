import random
nrOfItterations = 10000
win = 0
for _ in range(nrOfItterations):
    firstPart = random.random()
    secondPart = 1 - firstPart

    thirdPart = max(firstPart, secondPart) *random.random()
    if (firstPart > secondPart):
        firstPart -= thirdPart
    else:
        secondPart -= thirdPart
    if(firstPart + secondPart > thirdPart and firstPart + thirdPart > secondPart and secondPart + thirdPart > firstPart):
        win += 1

prob = win/nrOfItterations
print(prob)
