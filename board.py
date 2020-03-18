from itertools import product

from utils import get_connections

class Tile:
	def __init__(self, letter=''):
		self.letter = letter
		self.children = []

	def add_link(self, other):
		self.children.append(other)


class Board:
	def __init__(self, start_values):
		self.tiles = start_values
		W, H = start_values.shape
		self.coords = product(range(W), range(H))
		self.links = {c:[] for c in self.coords}

		self.link_tiles()

	def link_tiles(self):
		for tile in self.tiles:
			pass

	def solve(self, word_list):
		connections = get_connections(word_list)