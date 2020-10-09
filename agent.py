import playground

import random
import collections

qfile = "./Qvals/q_6x7.txt"

class Agent():
	Q = collections.defaultdict(int) # Q matrix

	def __init__(self, e=0.1, a=0.5, g=0.9):	
		self.epsilon = e # epsilon: for epsilon-greedy policy
		
		self.alpha = a # learning rate/average coefficient

		self.gamma = g # long-term reward factor

		return
	

	def _random_move(self, env):
		return random.choice(env.actions)
	

	def _export_Qval(self):
		try:
			F = open(qfile, 'w')

			for x in self.Q:
				F.write("%s %f\n" % (x, self.Q[x]))

		finally:
			F.close()
		
		return


	def _import_Qval(self):
		return 
	

	def _qlearning_move(self, env):
		# epsilon-greedy policy
		s = random.random() # seed

		if s < self.epsilon:
			return random.choice(env.actions)

		A = [self.Q[(env.state, a)] for a in env.actions] # all Q(s, a) vals
		
		M = max(A)

		act_M = [a for i, a in enumerate(env.actions) if A[i] == M]

		return random.choice(act_M)
	

	def _qupdate(self, s1, a1, s2, acts, reward):
		M = max(self.Q[(s2, a)] for a in acts)

		self.Q[(s1, a1)] += self.alpha * (reward + self.gamma * M - self.Q[(s1, a1)])

		return
	

	def update(self, s1, a1, s2, acts, reward):
		#return
		return self._qupdate(s1, a1, s2, acts, reward)
		
	def move(self, env):
		#return self._random_move(env)
		return self._qlearning_move(env)

	def record(self):
		self._export_Qval()
		return


