from math import exp
from random import randint as r
def sigmoid(x, h=1):
	if x >= 0:
		return h / (h + exp(-x))
	else:
		z = exp(x)
		return z / (h + z)

def mse(correct, atempt):
	return sum([(a-b)**2 for a, b in zip(correct, atempt)])/min(len(correct), len(atempt))

def chance(chance):
	return int((r(1, chance) == 1))

def npos(num):
	if r(0,1) == 1:
		return num
	return -num