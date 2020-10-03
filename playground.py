import numpy as np
import random

class Env():
	def __init__(self, n, m, k=4):
		self.n, self.m, self.k = n, m, k
		self.c = 0 # count of moves

		self.board = [[0]*m for _ in range(n)] # init
		
		self.state = (0, )*m

		self.act_ind = [0]*m # possible col index
		self.actions = [[i, self.act_ind[i]] for i in range(self.m)]


	def __str__(self):
		#return str(np.array(self.board[::-1])) # reverse to match the actual game
		return str(np.array(self.board)) 

	def _take_act(self):
		return random.choice(range(self.m))	


	def _reward(self, i, j):
		c = 0 # c: count
		t = self.board[i][j] # t: target
		B = [0]*7 # B: buffer

		for p, (u, v) in enumerate([(1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]): # check 7 directions
			s  = self.board[i+u][j+v] # s: sample
			if not s: # no stone
				continue
			
			k = 1
			
			while 0<= i+k*u < self.n and 0<= j+k*v < self.m \
				and self.board[i+k*u][j+k*v] == s and k <= self.k-1:
				
				c += 1
				k += 1

			B[p] = (k-1) * [-1, 1][s == t]

			if k == self.k and s == t: # winning bonus!
				c += self.m * self.n

		# deal with the case that the stone is in the middle of the line
		for p in range(3):
			if B[p] + B[p+4] + 1 >= self.k: 
				c += self.m * self.n

		return c


	def _i_state(self, j):
		b = 1 # start from 1
		
		i = 0
		while self.board[i][j]:
			b = (b << 1) + (self.board[i][j]-1)
			i += 1

		return b


	def step(self, act):
		# put a stone at col act
		i, j = self.act_ind[act], act

		b = self.c % 2 # b: stone bit
		self.board[i][j] = b + 1 # grid = 0: empty, 1: black, 2: white
		
		# n means no more room for stone
		self.act_ind[act] = min(self.act_ind[act]+1, self.n) 

		self.state = self.state[:j] + (self._i_state(j),) + self.state[j+1:]

		self.c += 1

		r = self._reward(i, j)

		return r, r >= self.n*self.m, {} 
		

	def reset(self, k=4, board=None):
		if not board:
			self.__init__(self.n, self.m, self.k)
		else:
			self.n, self.m, self.k = len(board), len(board[0]), k
			
			self.board = board

			self.state = tuple(self._i_state(i) for i in range(self.m))
			
			self.c = 0
			for j in range(self.m):
				i = 0
				while board[i][j]:
					i += 1
				
				self.c += i # update moves

				self.act_ind[j] = i # update action index

class Agent():
	def __init__(self):
		return

	def move(self, env):
		return 0		

