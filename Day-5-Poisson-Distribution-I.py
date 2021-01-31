from math import factorial, exp

miu = float(input())
x = int(input())
poisson_prob = ((miu ** x) * exp(-miu)) / factorial(x)
print("%.3f" %poisson_prob)


X = poisson random variable, ie, X ~ Po( miu )

x = number of successes that occur in a specified region

miu = mean number of successes that occur in a specified region

exp = constant = approximately 2.71828

P(X = x) = ((miu ** k) * exp(-miu)) / factorial(k)

