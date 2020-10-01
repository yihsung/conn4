import playground

g1 = playground.Game(6, 7)
g1.step(0)
g1.step(1)
g1.step(1)
print(g1)
print(g1.state)
print(g1.actions)
g1.reset()
print(g1)
print(g1.state)
