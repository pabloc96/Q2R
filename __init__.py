from . import Q2R as q2r

def make_automata(grid):
	"""
	Creates a Q2R cellular automata from a squared matrix (the grid).
	"""
	return q2r.Q2R(grid)

def rand(n, proportion = 0.5):
	"""
	Creates a Q2R cellular automata with a random nxn configuration matrix. The proportion of +1 is given by the proportion parameter.
	"""
	return q2r.Q2R(random_grid = n, proportion = proportion)

