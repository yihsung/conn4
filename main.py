import playground

b1 = ([[1, 2, 1, 2, 2, 1, 1], [2, 0, 0, 0, 0, 0, 0], 
	   [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]) 

print(b1)

g1 = playground.Env(6, 7)
p1, p2 = playground.Agent(), playground.Agent()

g1.step(0)
g1.step(1)
g1.step(1)
print(g1)
print(g1.state)
print(g1.act_ind)
g1.reset(board=b1)
print(g1.step(1))
print(g1)
print(g1.state)
print(g1._reward(1,1))

act = p1.move(g1)
g1.step(act[0])
act = p2.move(g1)
g1.step(act[0])
print(g1)
