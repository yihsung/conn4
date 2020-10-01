import numpy as np

class Game():
	def __init__(self, n, m):
		self.n, self.m = n, m
		self.c = 0 # count of moves

		self.board = [[0]*m for _ in range(n)] # init
		
		self.state = (0, )*m
		self.actions = [0]*m # possible index

	def __str__(self):
		return str(np.array(self.board))
	
	def step(self, act):
		# put a stone at col act

		b = self.c % 2
		self.board[self.actions[act]][act] = b + 1
		
		# n means no more room for stone
		self.actions[act] = min(self.actions[act]+1, self.n) 

		def i_state(j):
			b = 1 # start from 1
			
			i = 0
			while self.board[i][j]:
				b = (b << 1) + (self.board[i][j]-1)
				i += 1

			return b

		self.state = self.state[:act] + (i_state(act),) + self.state[act+1:]

		self.c += 1
		
	def reset(self):
		self.__init__(self.n, self.m)

