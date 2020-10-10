import playground

import random
import collections

qfile = "./Qvals/q_6x7.txt"

class Agent():
	Q = collections.defaultdict(int) # Q matrix

	def __init__(self, e=0.1, a=0.5, g=0.99):	
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
				# seprate s by " "; seprate s and a by ","; seprate (s,a) and Q by ":"
				t = " ".join(map(str, x[0])) + ", " + str(x[1]) 

				F.write("%s:%f\n" % (t, self.Q[x]))

		finally:
			F.close()
		
		return


	def _import_Qval(self):
		with open(qfile, 'r') as F:
			for line in F:
				data = line.split(":")

				s, a = data[0].split(",")
				
				s = tuple(int(x) for x in s.split(" "))
				a = int(a)

				self.Q[(s, a)] = float(data[1][:-2]) # [:-2] to remove the next line char, '\n'
		F.close()
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
		if not acts:
			print("!") # no more valid actions, i.e. the board is full
			return 1

		M = max(self.Q[(s2, a)] for a in acts)

		self.Q[(s1, a1)] += self.alpha * (reward + self.gamma * M - self.Q[(s1, a1)])

		return 0
	

	def update(self, s1, a1, s2, acts, reward):
		#return
		return self._qupdate(s1, a1, s2, acts, reward)
		
	def move(self, env):
		#return self._random_move(env)
		return self._qlearning_move(env)


	def load(self):
		self._import_Qval()
		return

	def record(self):
		self._export_Qval()
		return


