# coding: utf-8
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import webbrowser as wb


#------------------Funciones de Herramientas---------------------------------------------------!

def infoAdicional():
	messagebox.showinfo("Juego de Fuentes de Energía", "Versión: 1.0.0")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto Bajo Licencia Personal y la UPTT")

def avisoSalida():
	valor=messagebox.askokcancel("Salir", "Deseas Salir de la aplicación?")

	if valor==True:
		root.destroy()



def cerrarVentana():
	root.destroy()

#------------------  VENTANA PROPIEDADES --------------------------------------------------------!
root=Tk()
root.geometry("1020x1020+0+0")
root.title("Fuentes de Energía")
root.iconbitmap("Logoproyecto.ico")
root.config(bg='dark turquoise')
e3=tk.Label(root,text="Marca los cuadros con los tipos de energia que ves en la imagen", bg="black",fg="White")
e3.pack(padx=5,pady=5,ipadx=5,ipady=5)
imagen= PhotoImage(file="img/Logoproyecto.png")
logo = Label(root,image=imagen, padx=10, pady=0).place(x=0,y=0)
fondo=PhotoImage(file="img/tierra.png")
lbfondo=Label(root, image=fondo).place(x=200, y=200)

#--------------Funcion validar---------------------------------------------------------
hidraulica=IntVar()
nuclear=IntVar()
eolica=IntVar()
solar=IntVar()
quimica=IntVar()

def validarVentana():
	opcionEscogida=""
	if (hidraulica.get()==1):
		opcionEscogida+= " Hidráulica"
	if (nuclear.get()==1):
		opcionEscogida+= " Nuclear"
	if (eolica.get()==1):
		opcionEscogida+= " Eólica"
	if (solar.get()==1):
		opcionEscogida+= " Solar"
	if (quimica.get()==1):
		opcionEscogida+= " Quimica"

	textoFinal.config(text=opcionEscogida)

def verificarEnergia():
	correcta=""
	if(hidraulica.get()==1 and nuclear.get()==0 and solar.get()==1 and eolica.get()==1 and quimica.get()==0):
	#con este comando la ventana principal se minimiza
		root.iconify()
	#inicia la segunda ventana con sus componentes
		win=Toplevel()
		win.title("Respuestas")
		win.iconbitmap("Logoproyecto.ico")
		win.geometry("400x400+600+200")
		win.config(bg='green')
		e3=tk.Label(win,text="Las Respuestas son Correctas \n FELICIDADES!!!", bg="black",fg="White",font="Helvetica 20" )
		e3.pack(padx=5,pady=100,ipadx=5,ipady=20)
		frame1=Frame(win)
		frame1.pack()
		botoncerrar=tk.Button(win,text="Salir", bg="red",fg="white",padx=15, pady=20 ,command=win.quit)
		botoncerrar.pack()

	elif(hidraulica.get()==1 and nuclear.get()==1 and solar.get()==1 and eolica.get()==1 and quimica.get()==1):
		root.iconify()
	#inicia la segunda ventana con sus componentes
		win=Toplevel()
		win.title("Respuestas")
		win.iconbitmap("Logoproyecto.ico")
		win.geometry("600x400+600+200")
		win.config(bg='#DF3A3A')
		e3=tk.Label(win,text="Acabas de Seleccionar Todas las Respuestas!!\n Algunas respuestas son Incorrectas \n Dale CLIC a la X y \n Sigue Intentando!!!", bg="#891BDA",fg="White", font="Helvetica 15")
		e3.pack(padx=5,pady=100,ipadx=5,ipady=20)
		frame1=Frame(win)
		frame1.pack()

	
	elif(hidraulica.get()==1 or nuclear.get()==1 or solar.get()==1 or eolica.get()==1 or quimica.get()==1):
		messagebox.showwarning("Incorrecto", "Tus Respuestas son Incorrectas!! Aún te faltan más \nPero no te preocupes, Persiona aceptar y Vuelve a intertarlo!!! Ánimo!!!!")

	
	else:
		messagebox.showwarning("Debes Seleccionar", "No has seleccionado ninguna respuesta \n pero no te preocupes, Persiona aceptar y Vuelve a intertarlo!!! Ánimo!!!!")

def documentacion():
	wb.open_new(r'C:\Users\alber\Desktop\Python\Graficos\ProyectoFuentesdeEnergia\documentacion.txt')

frame=Frame(root)
frame.pack()


#------------------Barra de Herramientas---------------------------------------------------!

barraMenu=Menu(root)
root.config(menu=barraMenu, width=600, height=480)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Salir", command=avisoSalida)


archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Documentación", command=documentacion)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Versión", command=infoAdicional)

#--------------------------Forma de Mostrar Barras---------------------------------------------!!

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
#------------- Checkboxs -------------------------------------------------------------------------

Label(frame, text="Elige la cantidad de opciones que se adapte a la imagen:")

Checkbutton(frame, text="Energia Hidráulica", variable=hidraulica, onvalue=1, offvalue=0, command=validarVentana).pack()
Checkbutton(frame, text="Energia Nuclear", variable=nuclear, onvalue=1, offvalue=0, command=validarVentana).pack()
Checkbutton(frame, text="Energia Eólica", variable=eolica, onvalue=1, offvalue=0, command=validarVentana).pack()
Checkbutton(frame, text="Energia Solar", variable=solar, onvalue=1, offvalue=0, command=validarVentana).pack()
Checkbutton(frame, text="Energia Química", variable=quimica, onvalue=1, offvalue=0, command=validarVentana).pack()

textoFinal=Label(frame)
textoFinal.pack()

#Botones de la segunda Ventana
botonVerifica=tk.Button(root, text="Verificar", bg="blue",fg="white",padx=10, command=verificarEnergia)
botonVerifica.pack()

botonSiguiente=tk.Button(root,text="Salir", bg="red",fg="white",padx=10 ,command=avisoSalida)
botonSiguiente.pack()







root.mainloop()