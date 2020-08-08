import numpy as np

class Q2R():

	def __init__(self, grid = None, random_grid = 0, proportion = 0.5):
		
		if random_grid > 0:
			# grid = np.random.rand(random_grid, random_grid)
			# grid = grid.round()
			# grid[grid == 0] = -1
			grid = np.random.choice([-1,1],random_grid**2, p=[1-proportion, proportion]).reshape(random_grid, random_grid)
		else:
			grid = np.array(grid)
		
		self.n = grid.shape[0]
		if grid.all == None:
			self.grid = np.array([[0]*n]*n)	
		else:
			self.grid = np.array(grid)
	
	def __str__(self):
		return '\n'.join([' | '.join([str("%2i " % u) for u in row]) for row in self.grid])

	def vn_neighborhood(self,x, y):
		return [tuple(np.array([x, y])), tuple(np.array([x + 1, y]) % self.n),\
		tuple(np.array([x - 1, y]) % self.n), tuple(np.array([x, y + 1]) % self.n),\
		tuple(np.array([x, y - 1]) % self.n)]

	def f(self, x, y):
		neighborhood = self.vn_neighborhood(x,y)
		this_cell_xy = neighborhood[0]
		neighborhood = neighborhood[1:]

		total = sum([self.grid[neighbour[0], neighbour[1]] for neighbour in neighborhood])

		if total == 0:
			return -self.grid[this_cell_xy[0], this_cell_xy[1]]
		return self.grid[this_cell_xy[0], this_cell_xy[1]]

	def iterate(self, mode = "sequential", order = None):
		if mode == "parallel":	
			new_grid = np.array([[0]*self.n]*self.n)

			for i in range(self.n):
				for j in range(self.n):
					new_grid[i,j] = self.f(i,j)
			self.grid = np.copy(new_grid)
		else:
			if order is None or (not order.size == self.n**2):
				print("Iteration mode is not parallel but no order matrix was given. It was not iterated.")
			else:
				for i in order:
					j = 0
					while i >= self.n:
						j += 1
						i -= self.n
					#print(i,j)
					self.grid[j,i] = self.f(j,i)
