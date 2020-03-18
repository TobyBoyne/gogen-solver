from string import ascii_lowercase
from itertools import product

# the letter z is not found in gogen puzzles
lowercase_letters = ascii_lowercase[:-1]

def get_connections(word_list):
	"""Returns a dictionary of each letter in the alphabet, where the value is
	a set of all the letters that are linked to it based on a word list"""
	connections = {letter: set() for letter in lowercase_letters}
	for word in word_list:
		for i, c in enumerate(word[:-1]):
			connections[c].add(word[i + 1])
			connections[i + 1].add(c)

	return connections

def get_linked_coords(W, H):
	"""Returns a dictionary of each coordinate in the grid of size (W, H), and the list of all
	points that are directly linked to that coordinate (vertical, horizontal, diagonal)
	Converts from a geometrical board to an arbitrarily shape, considering only how adjecent tiles are connected"""
	linked_coords = set()
	for (x, y) in product(range(W), range(H)):
		pass