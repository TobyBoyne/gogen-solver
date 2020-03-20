import numpy as np

from board import Board

def test_board_typical():
	"""Test case for a typical 5x5 board
	Taken from http://www.puzzles.grosse.is-a-geek.com/images/gog/puz/uber/uber20200319sol.png"""
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

def test_board_irregular():
	"""Test case for a 5x5 board where the given letters are not in the typical tile spaces
	Taken from http://www.puzzles.grosse.is-a-geek.com/images/gog/puz/hyper/hyper20200319sol.png"""
	start_values = np.array([
			['',	'',		'',		'',		''],
			['q',	'',		'',		'',		'p'],
			['',	'',		'',		'',		''],
			['',	'',		'',		'',		''],
			['',	'',		'n',	'',		'g']
		])

	word_list = [
		'rtcw', 'clv', 'qxf', 'voga', 'qsh', 'yjg', 'tbio', 'kun', 'tskyi', 'fue', 'mfj'
	]

	expected_solution = np.array([
			['h',	'r',	't',	'c',	'w'],
			['q',	's',	'b',	'l',	'p'],
			['x',	'k',	'y',	'i',	'v'],
			['f',	'u',	'd',	'j',	'o'],
			['e',	'm',	'n',	'a',	'g']
		])

	board = Board(start_values, word_list)
	board.solve()

	assert np.char.equal(board.solution, expected_solution).all()