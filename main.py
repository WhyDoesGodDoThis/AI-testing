import network as n


data = [
	[189, 87],
	[195, 81],
	[155, 51],
	[191, 79],
	[172, 67],
	[185, 81],
	[168, 59],
	[153, 51],
	[181, 78],
	[188, 80]
]

ans = [
	0,
	0,
	0,
	0,
	1,
	1,
	1,
	1,
	0,
	1
]




net = n.network(6, 3)
for a in data:
	net.calculate(a)
carry = net.copy()
net = carry.copy()
net.outputs = []
print(carry.score(ans))
for i in range(10000):
	net.mutate(6)
	for a in data:
		net.calculate(a)
	if net.score(ans) < carry.score(ans):
		carry = net.copy()
		net = carry.copy()
		net.outputs = []
	else:
		net = carry.copy()
		net.outputs = []
	if i/1000 in range(10):
		print(carry.score(ans))