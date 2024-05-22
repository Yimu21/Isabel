from tkinter import *
#from tkinter import . messagebox


ventana =Tk()
ventana.title("uso de Radiobutton")
ventana.geometry("500x300")
ventana.config(bg="#87CEEB")
ventana.resizable=False

#variables

num    =IntVar()
opcion =IntVar()
total  =IntVar()
mostrar =StringVar()
def operacion():
    numero =num.get()
    if opcion.get()==1:
        total=numero*5;val=5
        print(numero)
    elif opcion.get()==2:
        total=numero * 10;val=10
    elif opcion.get()==3:
        total=numero * 20;val=20
    elif opcion.get()==4:
        total=numero *30;val=30
    else:
        total=numero *40;val=40
    mostrar.set(f"Resultado : {numero}x{val}={total}")


lbNumero = Label(ventana,text="Escriba un numero:",bg="#87CEEB", font="Curier 11 bold",fg="#DC143C")
lbNumero.place(x="20",y="20")

txNumero =Entry(ventana, textvariable=num,font="Helvetica 12", bd="5",justify="right")
txNumero.place(x="175",y="20")
txNumero.focus()

x5 =Radiobutton(ventana, text="x5",value=1,bg="#87CEEB", bd=5, variable=opcion)
x5.place(x="20",y="80")

x10 =Radiobutton(ventana, text="x10",value=2,bg="#87CEEB", bd=5, variable=opcion)
x10.place(x="70",y="80")

x20 =Radiobutton(ventana, text="x20",value=3,bg="#87CEEB", bd=5, variable=opcion)
x20.place(x="120",y="80")

x30 =Radiobutton(ventana, text="x30",value=4,bg="#87CEEB", bd=5, variable=opcion)
x30.place(x="170",y="80")

x40 =Radiobutton(ventana, text="x40",value=5,bg="#87CEEB",bd=5,variable=opcion)
x40.place(x="220",y="80")

btEjecutar = Button(ventana,text="Realizar la opercaion .",command=operacion)
btEjecutar.place(x="220",y="140")


lbSalida =Label(ventana, text="...",textvariable=mostrar, bg="#87CEEB" , font="Curier 11 bold")
lbSalida.place(x="220",y="180")

ventana.mainloop()











