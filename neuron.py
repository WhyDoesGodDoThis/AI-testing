from my_math import sigmoid as sig
from random import seed as s
from random import randint as r

def neuron(seed, inputs):
	s(seed)
	bais = r(-5, 5)
	return sig(sum([i*(r(-200, 200)/100) for i in inputs]) + bais)