import tkinter as tk
from tkinter import *

class Ask(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent, background="red", width=600)
		print("test")
		self.v = IntVar()
		self.crateFrame()



	def crateFrame(self):


		self.sourcePicture = tk.Canvas(self, width=100, height=100, background="green")
		self.sourcePicture.grid(row=1, column=0, rowspan=4, stick="w")

		self.sourcePicture = tk.Canvas(self, width=100, height=100, background="blue")
		self.sourcePicture.grid(row=1, column=3, rowspan=4, stick="e")

		self.radioOption1 = tk.Radiobutton(self, text="1", variable=self.v, value=0)
		self.radioOption2 = tk.Radiobutton(self, text="2", variable=self.v, value=1)
		self.radioOption3 = tk.Radiobutton(self, text="3", variable=self.v, value=2)
		self.radioOption4 = tk.Radiobutton(self, text="4", variable=self.v, value=3)

		self.radioOption1.grid(row=1, column=2, stick="w")
		self.radioOption2.grid(row=2, column=2, stick="w")
		self.radioOption3.grid(row=3, column=2, stick="w")
		self.radioOption4.grid(row=4, column=2, stick="ws")
		self.seperator = tk.Canvas(self, width=400, height=10)
		self.seperator.grid(row=0, column=0, columnspan=3, stick="w")
		self.seperator.create_line(0, 5, 100, 5, width=1, fill="gray")
