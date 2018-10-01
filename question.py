import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class Ask(tk.Frame):
	def __init__(self, parent, image1, image2):
		size = 100,100

		self.pimage1 = Image.open(image1)
		self.pimage1.thumbnail(size)
		self.pimage1= ImageTk.PhotoImage(self.pimage1)

		self.pimage2 = Image.open(image2)
		self.pimage2.thumbnail(size)
		self.pimage2= ImageTk.PhotoImage(self.pimage2)

		tk.Frame.__init__(self, parent, width=600)
		self.v = IntVar()
		self.crateFrame()

	def crateFrame(self):
		self.sourcePicture = tk.Canvas(self, width=100, height=100)
		self.sourcePicture.create_image(52, 52, image=self.pimage1)
		self.sourcePicture.grid(row=1, column=0, rowspan=4, stick="w")

		self.sourcePicture = tk.Canvas(self, width=100, height=100)
		self.sourcePicture.create_image(52, 52, image=self.pimage2)
		self.sourcePicture.grid(row=1, column=3, rowspan=4, stick="e")

		self.radioOption1 = tk.Radiobutton(self, text="do nothing", variable=self.v, value=0, width=30)
		self.radioOption2 = tk.Radiobutton(self, text="<- delete original file", variable=self.v, value=1, width=30)
		self.radioOption3 = tk.Radiobutton(self, text="delete files in sorted location ->", variable=self.v, value=2, width=30)
		self.radioOption4 = tk.Radiobutton(self, text="autorename file", variable=self.v, value=3, width=30)

		self.radioOption1.grid(row=1, column=2)
		self.radioOption2.grid(row=2, column=2)
		self.radioOption3.grid(row=3, column=2)
		self.radioOption4.grid(row=4, column=2)
		self.seperator = tk.Canvas(self, width=200, height=10)
		self.seperator.grid(row=0, column=0, columnspan=3, stick="w")
		self.seperator.create_line(0, 5, 100, 5, width=1, fill="gray")
