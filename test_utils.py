import utils
from utils import lowercase_letters
import pytest

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

def test_letter_to_num():
	assert utils.letter_to_num('b') == 1

	# test that a numerical input will raise an error
	with pytest.raises(TypeError):
		utils.letter_to_num(6)