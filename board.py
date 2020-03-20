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


	def get_adjecent_tiles(self):
		pass

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