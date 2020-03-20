from itertools import product
import numpy as np

from utils import get_connections

class Tile:
	def __init__(self, letter=''):
		self.letter = letter
		self.children = []
		self.possible_values = []

	def add_link(self, other):
		self.children.append(other)

	def __repr__(self):
		return f"Tile({self.letter})"

class Board:
	def __init__(self, start_values):
		self.tiles = np.empty_like(start_values, dtype=object)

		for y, row in enumerate(start_values):
			for x, value in enumerate(row):
				self.tiles[y, x] = Tile(value)


	def link_tiles(self):
		for tile in self.tiles:
			pass

	def solve(self, word_list):
		connections = get_connections(word_list)

if __name__ == "__main__":
	start_values = np.array([
		['a',	'',		'',		'',		'b'],
		['',	'',		'',		'',		''],
		['',	'',		'x',	'',		''],
		['',	'',		'',		'',		''],
		['c',	'',		'',		'',		'd']
	])

	board = Board(start_values)