from itertools import chain
import numpy as np

x = np.array([1, 0, 1])
y = np.array([0, 1, 1])
print(np.count_nonzero(x))
print((x & y))


from utils import get_connections, lowercase_letters, letter_to_num

class Board:
	"""A class to store the possible letter values as a 1D array for each space on a 2D grid.
	Contains solving logic"""
	def __init__(self, start_values):
		h, w = start_values.shape
		self.start_letters = set()

		self.tiles = np.ones((h, w, len(lowercase_letters)))

		for (x, y), letter in np.ndenumerate(start_values):
			if letter:
				i = letter_to_num(letter)
				self.solve_tile(x, y, i)
				self.start_letters.add((x, y, i))


	def create_letter_mask(self, x, y, j):
		"""Creates an AND mask centred around the point (x, y) so that the character stored in j can
		only be placed adjacent to (x, y)
		Used to apply a link between letters
		1 values form a 3x3x1 grid, and are 1 in every other slice"""
		mask = np.ones_like(self.tiles)
		# ensure that if x or y is 0, then index will remain positive
		x_low = max(x-1, 0)
		y_low = max(y-1, 0)

		mask[:, :, j] = 0
		mask[y_low:y+2, x_low:x+2, j] = 1
		return mask

	def create_tile_mask(self, x, y, i):
		"""Creates an AND mask at point (x, y), so that the tile cannot take on any other letter,
		and no other tile can take on the letter stored in the tile
		Used once a tile has been solved
		0 values form a 1x1x25, and a 5x5x1 grid
		Value at (x, y, i) must be 1"""
		mask = np.ones_like(self.tiles)

		mask[:, :, i] = 0
		mask[y, x, :] = 0
		mask[y, x, i] = 1
		return mask


	def check_letters_solved(self):
		"""Check if any of the letters can only be placed in exactly one tile - if so, that letter is solved
		Raise an error if the letter cannot be placed in any tile"""
		tile_count = np.count_nonzero(board.tiles,axis=(0, 1))
		if 0 in tile_count:
			ValueError(f"The letter(s) {np.argwhere(tile_count==0)} cannot be placed on the grid")

		solved_letters = np.argwhere(tile_count==1).flat
		out = []
		for i in solved_letters:
			y, x = np.argwhere(self.tiles[:, :, i])[0]
			out.append((x, y, i))
		return out

	def check_tiles_solved(self):
		"""Check if any of the tiles only have one possible letter that can be placed there
		Raise an error if any of the tiles cannot have any letter placed there"""
		letter_count = np.count_nonzero(self.tiles, axis=2)
		if 0 in letter_count:
			raise ValueError(f"No letter can be placed at the coordinate(s) {np.argwhere(letter_count==0)}")

		solved_tiles = np.argwhere(letter_count==1)
		out = []
		for y, x in solved_tiles:
			i = np.argwhere(self.tiles[y, x, :])[0][0]
			out.append((x, y, i))
		return out


	def solve_tile(self, x, y, i):
		"""Show that a single tile is solved by applying the mask"""
		mask = self.create_tile_mask(x, y, i)
		self.tiles = np.logical_and(self.tiles, mask)

	def solve(self, word_list):
		"""	Creates a dictionary where each letter is given a set of possiible spaces in which it can be placed.
		A letter with:
		 - no possible spaces will raise an error
		 - exactly one possible space will be placed there, and removed from dictionary
		 Through iteration and deduction, all letters will be placed"""
		connections = get_connections(word_list)
		solved_letters = self.start_letters
		new_solved_letters = self.start_letters
		# TODO: when there is no certain move, find the letter with the fewest possible positions and determine
		# - where the next may go
		# main solving loop - repeat until no more letters have been added
		while new_solved_letters:
			# use masks to find where new letters can be placed
			for x, y, i in new_solved_letters:
				for j in connections[i]:
					mask = self.create_letter_mask(x, y, j)
					self.tiles = np.logical_and(self.tiles, mask)

			# check if any tiles can now be solved
			new_solved_letters = set()
			for x, y, i in self.check_letters_solved() + self.check_tiles_solved():
				if (x, y, i) not in solved_letters:
					self.solve_tile(x, y, i)
					new_solved_letters.add((x, y, i))
					solved_letters.add((x, y, i))
			print(new_solved_letters, "\n\n\n")
		print(self.tiles)



if __name__ == "__main__":
	start_values = np.array([
		['r',	'',		'w',	'',		'y'],
		['',	'',		'',		'',		''],
		['s',	'',		'q',	'',		'n'],
		['',	'',		'',		'',		''],
		['p',	'',		'f',	'',		'k']
	])

	word_list = [
		'bio', 'deathful', 'drest', 'ghast', 'hades', 'loxes', 'phase', 'quoin', 'sajou', 'unmixed', 'vex'
	]

	board = Board(start_values)
	board.check_tiles_solved()

	board.solve(word_list)