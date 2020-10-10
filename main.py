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
player = [agent.Agent(), agent.Agent()]
episodes = 100000

player[0].load() # load Q-val

for _ in range(episodes):
	turn = 0
	g1.reset()

	while not g1.end:
		s1 = g1.state
		a1 = player[turn].move(g1)

		reward, _, __ = g1.step(a1)
		
		s2 = g1.state
		acts = g1.actions

		# if update fails, print out the board
		if player[turn].update(s1, a1, s2, acts, reward):
			print(g1)

		#print(g1.state)
		#print(player[turn].Q[(s1, a1)])
		turn = 1 - turn

	print(g1)
	print(2-turn) # winner = 1 - turn + 1

player[0].record() # record Q-val
