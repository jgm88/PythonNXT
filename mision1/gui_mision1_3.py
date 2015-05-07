#!/usr/bin/env python

from Tkinter import *
from PIL import Image, ImageTk
from mision1_3 import *

class Application:

	def __init__(self, root):

		self.root= root
		self.root.title= 'Mision 3'
		root.resizable(width=FALSE, height=FALSE)

		self.usb=True

		self.panel = PanedWindow(self.root, orient=VERTICAL)

		self.var= StringVar()
		self.mac= StringVar()
		self.mac.set("00:16:53:09:46:3B")
		self.var.set("Bluetooth")
		self.panel.add(Radiobutton(root, text="Usb", variable=self.var, value="Usb"))
		self.panel.add(Radiobutton(root, text="Bluetooth", variable=self.var, value="Bluetooth"))
		self.panel.add(Label(self.root, justify=LEFT, text="Mac address", font="Arial 12 bold"))
		self.panel.add(Entry(self.root, textvariable=self.mac))
		self.panel.add(Label(self.root, justify=LEFT, text="Mac obligatoria si desea conexion Bluetooth", font="Arial 12 bold"))
		self.panel.add(Button(root, text="Run mision", command=self.mision))
		self.panel.pack()

		self.canvas= Canvas(root)
		self.imagen= LabelFrame(self.root, text="Objetivo de la mision", padx=10, pady=10)
		self.imagen.pack(side=LEFT,fill="both", expand="yes", padx=10, pady=10)
		self.canvas = Canvas(self.imagen, width=640, height=480, bg="white")
		
		self.image= ImageTk.PhotoImage(Image.open('gui_mision13_img.png'))
		self.canvas.create_image(0,0,anchor=NW, image=self.image)
		self.canvas.pack()
	def callRobot(self, event):
		
		if(event.keysym == 'w'):
			self.robot.move(1)
		elif(event.keysym == 's'):
			self.robot.move(-1)

		# Girar a la derecha
		elif(event.keysym == 'a'):
			self.robot.turn(1)

		# Girar a la izquierda
		elif(event.keysym == 'd'):
			self.robot.turn(-1)

		# Brazo arriba
		elif(event.keysym == 'q'):									
			self.robot.arm.turn(40, 50)

		# Brazo abajo
		elif(event.keysym == 'e'):							
			self.robot.arm.turn(-40, 50)

		# Parar o activar motor
		elif(event.keysym == "space"):
			self.robot.stop()

		#Cerrar programa
		elif(event.keysym == 'p'):
			self.robot.syncMotor.brake()
			self.robot.arm.brake()	
			self.root.destroy()		

		# Acelerar
		elif(event.keysym == 'plus'):
			self.robot.speed(1)

		elif(event.keysym == 'minus'):
			self.robot.speed(-1)
	def mision(self):
		if self.var.get()=="Bluetooth" and self.mac.get()=="":
			return
		
		self.robot= Robot(connect(self.var.get(), self.mac.get()))		
		# self.robot.mision()

if __name__=='__main__':
	root= Tk()
	app = Application(root)
	app.mision()
	root.bind_all("<Key>", app.callRobot)
	root.mainloop()