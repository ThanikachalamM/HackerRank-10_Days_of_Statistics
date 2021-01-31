import math

mean, std = 70, 10
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

#grade >80
print('{:.2f}'.format((1 - cdf(80))* 100))
#grade >=60
print('{:.2f}'.format((1- cdf(60))* 100))
#grade <60
print('{:.2f}'.format(cdf(60)*100))