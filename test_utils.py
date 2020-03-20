import utils
from utils import lowercase_letters
import pytest

def test_get_connections():
	word_list = ['alpa', 'ca']
	connections = utils.get_connections(word_list)
	expected_connections = {i: set() for i in range(len(lowercase_letters))}
	result = {
		0: {11, 15, 2},
		11: {0, 15},
		15: {11, 0},
		2: {0}
	}
	expected_connections.update(result)

	assert connections == expected_connections

def test_letter_to_num():
	assert utils.letter_to_num('b') == 1

	# test that a numerical input will raise an error
	with pytest.raises(TypeError):
		utils.letter_to_num(6)