from itertools import product

class Tile:
	def __init__(self, letter=''):
		self.letter = letter
		self.children = []

	def add_link(self, other):
		self.children.append(other)