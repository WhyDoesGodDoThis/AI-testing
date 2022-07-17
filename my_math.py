from math import exp
def sigmoid(x):
	if x >= 0:
		return 1 / (1 + exp(-x))
	else:
		z = exp(x)
		return z / (1 + z)

def mse(correct, atempt):
	return sum([(a-b)**2 for a, b in zip(correct, atempt)])/min(len(correct), len(atempt))
	