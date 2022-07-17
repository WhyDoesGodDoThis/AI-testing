from network import network as n
from network import snetwork as sn
from random import randint as r
from random import random as ra

def npos(num):
	if bool(r(0,1)):
		return num
	return -num

def mrn(ans, inps):
	return n(ra(), r(2,9), ans, inps)

def msn(s, ans, inps):
	if s.hid < 3:
		hid = r(0,3)
	else:
		hid = r(-3, 3)
	return n(s.seed+npos(ra()), s.hid+hid, ans, inps)

def scr(nets):
	nets.sort(key=lambda x: x.score)
	return nets
carry = []
def run(gens, pop, inputs, answers):
	global carry
	all = [mrn(answers, inputs) for i in range(pop)]
	carry = scr(all)[0:4]
	for i in range(gens):
		all = [msn(carry[r(0,3)], answers, inputs)]
		carry = carry + scr(all)[0:4]
		carry = scr(carry)[0:4]
	c = carry[0]
	print(c.score, c.seed, c.hid)

def Main():
	i = [
  [-2, -1],  # Alice
  [25, 6],   # Bob
  [17, 4],   # Charlie
  [-15, -6], # Diana
	]
	o = [
  1, # Alice
  0, # Bob
  0, # Charlie
  1, # Diana
	]
	run(3000, 10, i, o)

if __name__ == "__main__":
	user = input(">>>")
	if user == '1':
		Main()
	else:
		user = input("AI data:").split(' ')
		net = sn(float(user[0]), int(user[1]))
		while True:
			net.test([int(zzz) for zzz in input("Test Data:").split(' ')])