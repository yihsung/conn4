import playground
import agent

b1 = ([[1, 2, 1, 2, 2, 1, 1], [2, 0, 0, 0, 0, 0, 0], 
	   [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]) 

g1 = playground.Env(6, 7)
p1, p2 = agent.Agent(), agent.Agent()

'''''
# test1
g1.step(0)
g1.step(1)
g1.step(1)
print(g1)
print(g1.state)
print(g1.act_ind)

# test2
g1.reset(board=b1)
print(g1.step(1))
print(g1)
print(g1.state)
print(g1._reward(1,1))

act = p1.move(g1)
print(act)
g1.step(act)
act = p2.move(g1)
g1.step(act)
print(g1)
'''''

# random game
print("----")
g1.reset()

turn = 0
while not g1.end:
	if turn == 0:
		g1.step(p1.move(g1))
	else:
		g1.step(p2.move(g1))

	turn = 1 - turn

print(g1)
print(2-turn) # winner = 1 - turn + 1

	

