import utils
from utils import lowercase_letters

def test_get_connections():
	word_list = ['alpha', 'beta']
	connections = utils.get_connections(word_list)
	expected_connections = {letter: {} for letter in lowercase_letters}
	result = {
		'a': {'l', 'h', 't'},
		'l': {'a', 'p'},
		'p': {'l', 'h'},
		'h': {'p', 'a'},
		'b': {'e'},
		'e': {'b', 't'},
		't': {'e', 'a'}
	}
	expected_connections.update(result)

	assert connections == expected_connections

def test_linked_coords():
	W, H = (2, 2)
	links = utils.get_linked_coords(W, H)
	# every point in a 2x2 grid is linked to every other point
	expected_links = {
		(0, 0): [(0, 1), (1, 0), (1, 1)],
		(0, 1): [(0, 0), (1, 0), (1, 1)],
		(1, 0): [(0, 1), (0, 0), (1, 1)],
		(1, 1): [(0, 1), (1, 0), (0, 0)]
	}

	assert links == expected_links