#!/usr/bin/env python

from Tkinter import *
import mision1_2

class Application:

	def __init__(self, root):

		self.root= root
		self.root.title= 'Mision 2'
		root.resizable(width=FALSE, height=FALSE)

		self.panel = PanedWindow(self.root, orient=VERTICAL)
		self.var= StringVar()
		self.mac= StringVar()
		self.radio= DoubleVar()
		self.var.set("Usb")
		self.panel.add(Radiobutton(root, text="Usb", variable=self.var, value="Usb"))
		self.panel.add(Radiobutton(root, text="Bluetooth", variable=self.var, value="Bluetooth"))
		
		self.panel.add(Label(self.root, justify=LEFT, text="Mac address, obligatoria si desea conexion Bluetooth", font="Arial 12 bold"))
		self.panel.add(Entry(self.root, textvariable=self.mac))

		self.panel.add(Label(self.root, justify=LEFT, text="Especificar radio del circulo", font="Arial 12 bold"))
		self.panel.add(Entry(self.root, textvariable=self.radio))
		
		self.panel.add(Button(root, text="Run mision", command=self.mision))
		self.panel.pack()

	def mision(self):
		if self.var.get()=="Bluetooth" and self.mac.get()=="":
			return

		if self.radio.get()==0.0:
			return

		robot= Robot(connect(self.var.get(), self.mac.get()))
		robot.mision(self.radio.get())

if __name__=='__main__':
	root= Tk()
	Application(root)
	root.mainloop()