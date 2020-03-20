import tkinter as tk
import numpy as np
from itertools import product
from utils import lowercase_letters

from board import Board

def single_lowercase_letter(s):
	"""Validates input in each square so that only one lowercase letter can be added to each Entry"""
	return len(s) <= 1 and s in lowercase_letters

def valid_word_list(s):
	"""Validates word list so that only lowercase letters and commas can be added"""
	return all(c in lowercase_letters + ', ' for c in s)


class UserInterface(tk.Frame):
	"""A class for the tkinter user interface for the program, as well as logic for passing the input to
	the Board class and displaying the solution"""
	def __init__(self, parent, size, **kwargs):
		tk.Frame.__init__(self, parent, **kwargs)
		self.size = size

		# create board attribute to be set after solving begins
		self.board = None

		# add Entry to allow text to be added in grid shape
		self.entries = []
		for x, y in product(range(size[0]), range(size[1])):
			entry = tk.Entry(self)
			self.entries.append(entry)
			entry.config(font=("Arial", 44), width=2, justify=tk.CENTER,
						 validate="key",
						 vcmd=(entry.register(single_lowercase_letter), '%P'))
			entry.grid(row=x, column=y)

		# add Entry to allow word list to be entered
		# and a Scrollbar so that all the words can be seen
		self.words_entry = tk.Entry(self)
		scroll = tk.Scrollbar(self)

		scroll.config(command=self.words_entry.xview, orient=tk.HORIZONTAL)
		self.words_entry.config(font=("Arial", 20),
							validate="key",
							vcmd=(self.words_entry.register(valid_word_list), '%S'),
							xscrollcommand=scroll.set)

		self.words_entry.grid(columnspan=5, stick=tk.NSEW)
		scroll.grid(columnspan=5, stick=tk.NSEW)

		# create a Button that will store the solution
		b = tk.Button(self)
		b.config(text="Solve", font=("Arial", 44),
				 command=self.read_and_solve)
		b.grid(columnspan=5, sticky=tk.NSEW)

	def read_and_solve(self):
		"""Get values from grid entried and the words list"""
		values = np.array([e.get() for e in self.entries])
		values = values.reshape(self.size)

		words = self.words_entry.get().replace(' ', '')
		word_list = words.split(',')

		self.board = Board(values, word_list)
		self.board.solve()
		self.display_solution()

	def display_solution(self):
		"""Insert solution values into the UI grid"""
		soln = self.board.solution
		for c, entry in zip(soln.flat, self.entries):
			entry.insert(0, c)

if __name__ == "__main__":
	master = tk.Tk()
	print(master.title("Gogen Solver"))
	UserInterface(master, (5, 5)).grid()
	master.mainloop()