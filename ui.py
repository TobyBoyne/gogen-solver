import tkinter as tk
from itertools import product
from utils import lowercase_letters

def single_lowercase_letter(s):
	"""Validates input in each square so that only one lowercase letter can be added to each Entry"""
	return len(s) <= 1 and s in lowercase_letters


def create_UI(W, H):
	window = tk.Tk()
	entries = []
	for (x, y) in product(range(W), range(H)):
		entry = tk.Entry()
		entries.append(entry)
		entry.config(font=32, width=2,
					 validate="key",
					 vcmd=(entry.register(single_lowercase_letter), '%P'))
		entry.grid(row=x, column=y)
	return window

if __name__ == "__main__":
	master = create_UI(5, 5)
	master.mainloop()