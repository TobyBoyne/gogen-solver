import tkinter as tk
import numpy as np
from itertools import product
from utils import lowercase_letters

def single_lowercase_letter(s):
	"""Validates input in each square so that only one lowercase letter can be added to each Entry"""
	return len(s) <= 1 and s in lowercase_letters

class UserInterface(tk.Frame):
	def __init__(self, parent, size, *args, **kwargs):
		tk.Frame.__init__(self, parent, **kwargs)
		# self.label = tk.Label(text="Hello, world")
		# self.label.pack(padx=10, pady=10)
		entries = []
		for x, y in product(range(size[0]), range(size[1])):
			entry = tk.Entry()
			entries.append(entry)
			entry.config(font=("Arial", 44), width=2, justify=tk.CENTER,
						 validate="key",
						 vcmd=(entry.register(single_lowercase_letter), '%P'))
			entry.grid(row=x, column=y)
			

if __name__ == "__main__":
	master = tk.Tk()
	UserInterface(master, (5, 5)).grid()
	master.mainloop()