import playground
import random

class Agent():
	def __init__(self):
		return
	

	def _random_move(self, env):
		return random.choice(env.actions)
		

	def move(self, env):
		return self._random_move(env)
