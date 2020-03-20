import numpy as np

from board import Board

def test_board_5x5():
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

	expected_solution = np.array([
			['r',	'v',	'w',	'b',	'y'],
			['d',	'e',	'x',	'i',	'm'],
			['s',	'a',	'q',	'o',	'n'],
			['t',	'h',	'j',	'u',	'l'],
			['p',	'g',	'f',	'c',	'k']
		])

	board = Board(start_values, word_list)
	board.solve()

	assert np.char.equal(board.solution, expected_solution).all()