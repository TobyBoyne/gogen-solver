import tkinter as tk
from itertools import product

def create_UI(W, H):
	window = tk.Tk()
	entries = []
	for (x, y) in product(range(W), range(H)):
		entry = tk.Entry()
		entries.append(entry)
		entry.config(font=32, width=2)
		entry.grid(row=x, column=y)
	return window

if __name__ == "__main__":
	master = create_UI(5, 5)
	master.mainloop()