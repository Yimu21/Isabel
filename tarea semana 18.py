
from tkinter import *
#ventana
ventana =Tk()
ventana.title("Uso de Radiobutton")
ventana.geometry("500x300")
ventana.config(bg="#87CEEB")
ventana.resizable=False

#variables

ventana = StringVar()
opcion =IntVar()
nombre =IntVar
num = IntVar()
venta =IntVar()
ventas =IntVar

def mostrarDatos():
    op =opcion.get()
    venta = ventas.get()
    if op ==1:
        sueldoBase =200
    elif op == 2:
        sueldoBase =250
    elif op == 3:
        sueldoBase =300

    if ventas > 0 and ventas < 1000:
        comision = ventas


    
nombre= Label(ventana,text="Escriba el nombre del vendedor:",bg="#87CEEB", font="Curier 11 bold",fg="#DC143C")
nombre.place(x="20",y="20")

txnombre =Entry(ventana, txnombre=num,font="Helvetica 12", bd="5",justify="right")
txnombre.place(x="175",y="20")
txnombre.focus()

catA =Radiobutton(ventana, text="x5",value=1,bg="#87CEEB", bd=5, variable=opcion)
catA.place(x="20",y="80")

catB =Radiobutton(ventana, text="x10",value=2,bg="#87CEEB", bd=5, variable=opcion)
catB.place(x="70",y="80")



#para ejecutar 
btEjecutar = Button(ventana,text="Realizar la opercaion .",command=operacion)
btEjecutar.place(x="220",y="140")

#salidad
lbSalida =Label(ventana, text="...",textvariable=mostrar, bg="#87CEEB" , font="Curier 11 bold")
lbSalida.place(x="220",y="180")

ventana.mainloop()