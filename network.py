from neuron import neuron as n
from random import randint as r
from random import random as ra
from random import seed as s
from my_math import mse

def net(seed, hiddens, inputs):
	s(seed)
	x = inputs
	for i in range(hiddens):
		x = [n(ra(), x) for y in range(r(3,8))]
	return n(ra(), x)

class network:
	def __init__(self, seed, h, ans, inps):
		self.seed = seed
		self.hid = h
		self.out = [net(seed, h, i) for i in inps]
		try:
			self.out = [sum(x) for x in self.out]
		except:
			pass
		self.score = mse(ans, self.out)

class snetwork:
	def __init__(self, seed, h):
		self.seed = seed
		self.hid = h
	def test(self, i):
		self.out = net(self.seed, self.hid, i)
		print(self.out)