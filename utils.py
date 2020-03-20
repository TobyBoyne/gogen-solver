from string import ascii_lowercase
from itertools import product

# the letter z is not found in gogen puzzles
lowercase_letters = ascii_lowercase[:-1]

def get_connections(word_list):
	"""Returns a dictionary of each letter in the alphabet, where the value is
	a set of all the letters that are linked to it based on a word list"""
	connections = {letter: set() for letter in lowercase_letters}
	for word in word_list:
		for i, c in enumerate(word[:-1]):
			connections[c].add(word[i + 1])
			connections[word[i + 1]].add(c)

	return connections

def letter_to_num(letter):
	return ord(letter) - 97