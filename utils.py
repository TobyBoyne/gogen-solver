from string import ascii_lowercase
from itertools import product

# the letter z is not found in gogen puzzles
lowercase_letters = ascii_lowercase[:-1]


def get_connections(word_list):
	"""Returns a dictionary of each letter in the alphabet, where the value is
	a set of all the letters that are linked to it based on a word list
	Each letter is stored as its letter_to_num value"""
	connections = {i: set() for i in range(len(lowercase_letters))}
	for word in word_list:
		num_word = [letter_to_num(c) for c in word]
		for i, c in enumerate(num_word[:-1]):
			connections[c].add(num_word[i + 1])
			connections[num_word[i + 1]].add(c)

	return connections

def letter_to_num(letter):
	return ord(letter) - 97

def num_to_letter(n):
	return chr(n + 97)

print([letter_to_num(c) for c in 'alpaca'])
