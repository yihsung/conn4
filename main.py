import playground

b1 = ([[1, 2, 1, 2, 2, 1, 1], [2, 0, 0, 0, 0, 0, 0], 
	   [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]) 

print(b1)

g1 = playground.Environ(6, 7)
g1.step(0)
g1.step(1)
g1.step(1)
print(g1)
print(g1.state)
print(g1.actions)
g1.reset(board=b1)
print(g1.step(1))
print(g1)
print(g1.state)
print(g1._reward(1,1))

