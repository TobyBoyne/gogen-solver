from itertools import product
import numpy as np

from utils import get_connections

class Tile:
	def __init__(self, letter=''):
		self.letter = letter
		self.children = []
		self.possible_values = []


	def __repr__(self):
		return f"Tile({self.letter})"

class Board:
	"""A class to store the letter values of each space as a Tile object. Contains solving logic"""
	def __init__(self, start_values):
		self.tiles = np.empty_like(start_values, dtype=object)

		for y, row in enumerate(start_values):
			for x, value in enumerate(row):
				self.tiles[y, x] = Tile(value)


	def get_adjacent_tiles(self, x, y):
		"""Returns a list of all adjacent tiles to a given coordinate"""
		sub_grid = self.tiles[y-1:y+1, x-1:x+1]
		centre_tile = self.tiles[y, x]
		adjacent_tiles = [t for t in sub_grid.flat if t is not centre_tile]
		return adjacent_tiles

	def solve(self, word_list):
		"""	Creates a dictionary where each letter is given a list of possiible	spaces in which it can be placed.
		A letter with:
		 - no possible spaces will raise an error
		 - exactly one possible space will be placed there, and removed from dictionary
		 Through iteration and deduction, all letters will be placed"""
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