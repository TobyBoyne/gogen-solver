from string import ascii_lowercase

# the letter z is not found in gogen puzzles
lowercase_letters = ascii_lowercase[:-1]

def get_connections(word_list):
	"""Returns a dictionary of each letter in the alphabet, where the value is
	a set of all the letters that are linked to it based on a word list"""
	connections = {letter: {} for letter in lowercase_letters}
	for word in word_list:
		for i, c in enumerate(word[:-1]):
			connections[c].add(word[i + 1])
			connections[i + 1].add(c)

	return connections