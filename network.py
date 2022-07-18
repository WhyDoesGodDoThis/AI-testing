import my_math as m
import random as r

class neuron:
	def __init__(self, inputs):
		self.weights = [1 for i in range(inputs)]
		self.bais = 1
	def calculate(self, inputs):
		return m.sigmoid(sum([a*b for a, b in zip(inputs, self.weights)]) + self.bais)
	def mutate(self):
		self.weights = [a+(m.chance(20)*m.npos(r.random())) for a in self.weights]
		self.bais = self.bais +(m.chance(20)*m.npos(r.randint(-2,2)))

class network:
	def __init__(self, length, inputs):
		self.len = length
		self.inps = inputs
		self.neurons = [[neuron(inputs) for i in range(4)]]
		self.neurons = self.neurons + [[neuron(4) for i in range(4)] for i in range(length-1)]
		self.outputs = []
		self.neurons.append([neuron(4)])
	def calculate(self, inputs):
		prev_data = inputs
		for i in self.neurons:
			prev_data = [a.calculate(prev_data) for a in i]
		self.outputs.append(prev_data[-1])
		return self.outputs[-1]
	def mutate(self, nmc):
		for a in self.neurons:
			for b in a:
				if bool(m.chance(nmc)):
					b.mutate()
	def copy(self):
		net = network(self.len, self.inps)
		net.neurons = self.neurons
		net.outputs = self.outputs
		return net
	def score(self, data_right):
		return m.mse(self.outputs, data_right)