from ui import single_lowercase_letter

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