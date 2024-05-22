
from tkinter import *

ventana =Tk()
ventana.title("Mi ventana en Tkinter")
ventana.geometry("500x300")
#ventana.iconbitmap("w.ico")
ventana.config(bg="#AAB7B8")

def mostrarDatos():
    Label(ventana,text=f"Tu nombre es : {txNombre.get()} {txApellido.get()} tu edad es :{txedad.get()} años").place(x="100",y="210") 
    if float(txedad.get()) < 18:
        Label(ventana,text=f"Eres menor de edad").place(x="100",y="240") 
    elif float(txedad.get()) >=18:
        Label(ventana,text=f"Eres mayor de edad").place(x="100",y="240") 

lbRotulo = Label(ventana,
                 text="Determinar si es mayor de edad o no",
                 bg="#5D6D7E",
                 bd="5",
                 fg="black",
                 padx="10",
                 pady="20",
                 font="consola 12 bold",
                 relief="ridge"
                 )
lbRotulo.pack(padx="5",pady="20")
lbNombre =Label(ventana,
                text="Ingrese su nombre ",
                bg="#5D6D7E")
lbNombre.place(x="100" , y="90")
txNombre =Entry()
txNombre.place(x="220",y="90")

lbApellido =Label(ventana,
                text="Ingrese su apellido ",
                bg="#5D6D7E")
lbApellido.place(x="100" , y="120")
txApellido =Entry()
txApellido.place(x="220",y="120")

lbedad =Label(ventana,
                text="Ingrese su edad ",
                bg="#5D6D7E",)
lbedad.place(x="100" , y="150")
txedad =Entry(width="5")
txedad.place(x="220",y="150")

btEjecutar =Button(ventana,
                  text="Ejecutar ",
                  bg="#5D6D7E",
                  bd=5,
                  command=mostrarDatos
                  )
btEjecutar.place(x="100",y="170")



btCerrar =Button(ventana,
                  text="Cerrar la ventana",
                  bg="#5D6D7E",
                  bd=5,
                  command=ventana.destroy
                  )
btCerrar.place(x="390",y="265")

ventana.mainloop()