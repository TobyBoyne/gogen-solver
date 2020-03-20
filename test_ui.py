from ui import single_lowercase_letter, valid_word_list

def test_single_lowercase_letter():
	test_inputs = (
		('a', True),
		('', True),
		('X', False),
		('ab', False),
		('2', False)
	)

	for s, expected_output in test_inputs:
		assert single_lowercase_letter(s) == expected_output

def test_valid_word_list():
	test_inputs = (
		('a', True),
		('', True),
		(', b', True),
		('cd', True),
		('2', False),
		('x?', False)
	)

	for s, expected_output in test_inputs:
		assert valid_word_list(s) == expected_output