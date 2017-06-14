from tkinter import *
import tkinter as tkk
from tkinter import messagebox as tkMessageBox

#Creacion de la ventana.
root = tkk.Tk()
root.title("Calculadora")
#Se le da un tamaño y posicion inicial a la ventana .
root.geometry("300x180+500+200")
#Se limita el tamaño a unico.
root.maxsize(300,180)
root.minsize(300,180)
#Funciones para botones de numeros
def Inserta1():
    _nombre=caja.get()
    caja.insert(len(_nombre),"1")
def Inserta2():
    _nombre=caja.get()
    caja.insert(len(_nombre),"2")
def Inserta3():
    _nombre=caja.get()
    caja.insert(len(_nombre),"3")
def Inserta4():
    _nombre=caja.get()
    caja.insert(len(_nombre),"4")
def Inserta5():
    _nombre=caja.get()
    caja.insert(len(_nombre),"5")
def Inserta6():
    _nombre=caja.get()
    caja.insert(len(_nombre),"6")
def Inserta7():
    _nombre=caja.get()
    caja.insert(len(_nombre),"7")
def Inserta8():
    _nombre=caja.get()
    caja.insert(len(_nombre),"8")
def Inserta9():
    _nombre=caja.get()
    caja.insert(len(_nombre),"9")
def Inserta0():
    _nombre=caja.get()
    caja.insert(len(_nombre),"0")
#Funciones para botones de operaciones
def Sumas():
    _nombre=caja.get()
    caja.insert(len(_nombre),"+")
def Restas():
    _nombre=caja.get()
    caja.insert(len(_nombre),"-")
def Divisiones():
    _nombre=caja.get()
    caja.insert(len(_nombre),"/")
def Multiplicaciones():
    _nombre=caja.get()
    caja.insert(len(_nombre),"*")
#Funcion que bota un resultado
def calculaRes():
    try:
        expresion=caja.get()
        caja.delete(0,END)
        res=eval(expresion)
        caja.insert(END,res)
    except:
        caja.insert(END, "Hubo un error intente nuevamente")
def borratodo():
    caja.delete(0,END)

#Creacion de el frame para contener los numeros
botonesnumeros=Frame(root)
botonesnumeros.place(x=10,y=10)
#Creacion de los numeros.
numero1=Button(botonesnumeros,text="1",command=Inserta1 ,width=3, height=2).grid(row=1,column=1)
numero2=Button(botonesnumeros,text="2",command=Inserta2,width=3, height=2).grid(row=1,column=2)
numero3=Button(botonesnumeros,text="3",command=Inserta3,width=3, height=2).grid(row=1,column=3)

numero4=Button(botonesnumeros,text="4",command=Inserta4 ,width=3, height=2).grid(row=2,column=1)
numero5=Button(botonesnumeros,text="5",command=Inserta5,width=3, height=2).grid(row=2,column=2)
numero6=Button(botonesnumeros,text="6",command=Inserta6,width=3, height=2).grid(row=2,column=3)

numero7=Button(botonesnumeros,text="7",command=Inserta7 ,width=3, height=2).grid(row=3,column=1)
numero8=Button(botonesnumeros,text="8",command=Inserta8,width=3, height=2).grid(row=3,column=2)
numero9=Button(botonesnumeros,text="9",command=Inserta9,width=3, height=2).grid(row=3,column=3)

numero0=Button(botonesnumeros,text="0",command=Inserta0,width=3, height=2).grid(row=4,column=2)
#Creacion de operadores como + -  * /
botonesoperandos=Frame(root)
botonesoperandos.place(x=150,y=51)
suma=Button(botonesoperandos,text="+",command=Sumas).grid(row=1,column=1)
resta=Button(botonesoperandos,text="-",command=Restas).grid(row=1,column=2)
division=Button(botonesoperandos,text="/",command=Divisiones).grid(row=2,column=1)
multpl=Button(botonesoperandos,text="*",command=Multiplicaciones).grid(row=2,column=2)

Igual=Button(botonesoperandos,text="=",command=calculaRes).grid(row=3,column=1)

#Etiqueta para dar el resultado.

label1=Label(root,text="resultado",cursor="pirate").place(x=105,y=10)

#Funcion que permite obtener el valor de la caja de entrada y mostrarlo posteriormente.
def Eliminarcaracteres():
    _nombre=caja.get()
    #Muestra una ventana extra con el valor entrante
    """tkMessageBox.askquestion("mensaje", "Ingresaste  %s"%_nombre)"""
    caja.delete(len(_nombre)-1)

#Creacion de la captura de los datos.
variable_string=StringVar()
caja=Entry(root,textvar=variable_string)
caja.place(x=160,y=10)
#Boton que permite la eliminacion de caracteres desde el final de la entrada,uno por uno.
boton=Button(root,text="<--",command=Eliminarcaracteres).place(x=250,y=51)
#Boton que elimina todo el display
botonb=Button(root,text="C",command=borratodo).place(x=200,y=51)
root.mainloop()
