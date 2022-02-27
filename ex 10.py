import random
import math


dayWillpay = round(0.02*740) #nr of times when he will pay 100% 2 lei
nrOfTimesRemaind = 740 - dayWillpay
suma = 0
for i in range(nrOfTimesRemaind + 1):

    a = (math.factorial(nrOfTimesRemaind)/(math.factorial(i)*math.factorial(nrOfTimesRemaind - i)))\
        * 0.05**i * 0.95**(nrOfTimesRemaind - i)

    if( i == 1):
        suma += a * 50
    if(i == 2):
        suma += a * 200
    if( i >= 3):
        suma +=(200 + 300*(i - 2))*a

expValueofpaying = 0.02 * 2 * dayWillpay
costOfaRide = suma/740 + expValueofpaying
print(costOfaRide)





