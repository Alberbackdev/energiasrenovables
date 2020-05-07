# coding: utf-8

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk


#------------------Funciones de Herramientas---------------------------------------------------!

def infoAdicional():
	messagebox.showinfo("Juego de Fuentes de Energía", "Versión: 1.0.0")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto Bajo Licencia GNU")

def avisoSalida():
	valor=messagebox.askokcancel("Salir", "Deseas Salir de la aplicación")


	if valor==True:
		root.destroy()


def abreFichero():
	fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Juegos Guardados", "*.py"),
		("Fichero de Texto", "*.txt"), ("Todos Los Ficheros", "*.*")))

	print(fichero)

def ventanaJuego():
	#con este comando la ventana se minimiza
	root.iconify()
	#inicia la segunda ventana con sus componentes
	win=Toplevel()
	win.title("Juego en Curso")
	win.iconbitmap("Logoproyecto.ico")
	win.geometry("950x750+0+0")
	win.config(bg='dark turquoise')
	e3=tk.Label(win,text="¿QUE TIPO DE ENERGÍA VES EN LA IMAGEN?", bg="black",fg="White")
	e3.pack(padx=5,pady=5,ipadx=5,ipady=5)
	
	#foto=PhotoImage(file="Logoproyecto.jpg")
	#lbfondo=Label(win, image=fondo).grid(row=0, column=0)

	frame=Frame(win)
	frame.pack()
	fondo=PhotoImage(file="img/tierra.png")
	lbfondo=Label(frame, image=fondo).pack(side=TOP)

	Label(frame, text="Elige la cantidad de opciones que se adapte a la imagen:")

	Checkbutton(frame, text="Energía Hidráulica").pack()
	Checkbutton(frame, text="Energía Quimica").pack()
	Checkbutton(frame, text="Energía Nuclear").pack()
	Checkbutton(frame, text="Energía Eolica").pack()
	Checkbutton(frame, text="Energía Solar").pack()


	#Botones de la segunda Ventana
	botonSiguiente=tk.Button(win,text="Siguiente",fg="green",padx=30, pady=15, command=ventana2)
	botonSiguiente.pack(side=tk.BOTTOM)
	
	boton2=tk.Button(win,text="Salir", fg="red", padx=30, pady=15, font="Helvetica 20", command=win.quit)
	boton2.pack(side=tk.BOTTOM)





def cerrarVentana():
	root.destroy()



#------------------  VENTANA PROPIEDADES --------------------------------------------------------!
root=Tk()
root.geometry("1024x750+0+0")
root.title("Fuentes de Energía")
root.iconbitmap("Logoproyecto.ico")
root.config(bg="blue", )
fondo=PhotoImage(file="img/distri.png")
lbfondo=Label(root, image=fondo).place(x=0,y=0)
imagen= PhotoImage(file="img/Logoproyecto.png")
logo = Label(root,image=imagen, padx=10, pady=10).place(x=0,y=0)

#------------------Barra de Herramientas---------------------------------------------------!

barraMenu=Menu(root)
root.config(menu=barraMenu, width=600, height=480)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir", command=abreFichero)
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Salir", command=avisoSalida)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)
archivoHerramientas.add_command(label="Seleccionar")
archivoHerramientas.add_command(label="Borrar")
archivoHerramientas.add_command(label="Borrar Todo")

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Documentación")
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Versión", command=infoAdicional)

#--------------------------Forma de Mostrar Barras---------------------------------------------!!

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edición", menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


#-----------------------Botones Pantalla Comenzar------------------------------------------!
botonComenzar=Button(root, text="Comenzar",bg="green",fg="white",command=ventanaJuego)
botonComenzar.pack(side=TOP)

#-----------------------Botones pantalla: Salir------------------------------------------!
botonSalir=Button(root, text="Salir", bg="red", fg="white", command=cerrarVentana)
botonSalir.pack(side=TOP)

#---------------------Ventana------------------------------------------------!














root.mainloop()