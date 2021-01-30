def g(n,p):
	return p * (1- p) ** (n - 1)
ko, total = map(int, input().split())
n=int(input())
r=g(n,ko/total)
print("%.3f" % r)
