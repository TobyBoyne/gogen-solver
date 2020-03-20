import utils
from utils import lowercase_letters

def test_get_connections():
	word_list = ['alpha', 'beta']
	connections = utils.get_connections(word_list)
	expected_connections = {letter: set() for letter in lowercase_letters}
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