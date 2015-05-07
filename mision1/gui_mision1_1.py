#!/usr/bin/env python

from Tkinter import *
from PIL import Image, ImageTk
from mision1_1 import *

class Application:

	def __init__(self, root):

		self.root= root
		self.root.title= 'Mision 1'
		root.resizable(width=FALSE, height=FALSE)
		self.panel = PanedWindow(self.root, orient=VERTICAL)
		self.var= StringVar()
		self.mac= StringVar()
		self.connect= IntVar()
		self.var.set("Usb")
		self.connect.set(0)
		self.panel.add(Radiobutton(root, text="Usb", variable=self.var, value="Usb"))
		self.panel.add(Radiobutton(root, text="Bluetooth", variable=self.var, value="Bluetooth"))
		self.panel.add(Label(self.root, justify=LEFT, text="Mac address", font="Arial 12 bold"))
		self.panel.add(Entry(self.root, textvariable=self.mac))
		self.panel.add(Label(self.root, justify=LEFT, text="Mac obligatoria si desea conexion Bluetooth", font="Arial 12 bold"))
		self.panel.add(Button(root, text="Run mision", command=self.mision))
		self.panel.add(Button(root, text="Run mision optional (Hacer recorrido de final a inicio al reves)", command=self.mision))
		self.panel.pack()

		self.canvas= Canvas(root)
		self.imagen= LabelFrame(self.root, text="Objetivo de la mision", padx=10, pady=10)
		self.imagen.pack(side=LEFT,fill="both", expand="yes", padx=10, pady=10)
		self.canvas = Canvas(self.imagen, width=640, height=480, bg="white")
		
		self.image= ImageTk.PhotoImage(Image.open('gui_mision11_img.png'))
		self.canvas.create_image(0,0,anchor=NW, image=self.image)
		self.canvas.pack()

	def mision(self):
		if self.var.get()=="Bluetooth" and self.mac.get()=="":
			return

		try :
			if self.connect.get()==0 :
				self.robot= Robot(connect(self.var.get(), self.mac.get()))
				self.connect.set(1)
			else:
				self.robot.mision()
		except ValueError:
			print "Cannot connect to robot"

	def optional(self):

		if self.var.get()=="Bluetooth" and self.mac.get()=="":
			return

		try:
			if self.connect.get()==0:
				self.robot= Robot(connect(self.var.get(), self.mac.get()))
				self.connect.set(1)
			else:
				robot.optional()
		except ValueError:
			print "Cannot connect to robot"


if __name__=='__main__':
	root= Tk()
	Application(root)
	root.mainloop()