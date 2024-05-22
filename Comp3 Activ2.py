from tkinter import * 

ventana = Tk() 
ventana.title("Cálculo del sueldo mensual en Tkinter")
ventana.geometry("850x480")
ventana.config(bg="#B1B2C7", cursor="man")
ventana.resizable(0,0)

nombre = StringVar()
categoría = StringVar
opcion = IntVar()
ventas = DoubleVar()
sueldoBase = DoubleVar()
comision = DoubleVar()
sueldoTotal = DoubleVar()

def mostrarDatos():
    op = opcion.get()
    venta = ventas.get()
    if op == 1:
        categoría = "A"
        sueldoBase = 200
    elif op == 2:
        categoría = "B"
        sueldoBase = 250
    elif op == 3:
        categoría = "C"
        sueldoBase = 300
    
    if (float(venta) > 0.01) and (float(venta) <= 1000):
        comision = round(float(venta) * 0.10, 2)
    elif (float(venta) > 1000) and (float(venta) <= 2000):
        comision = round(float(venta) * 0.20, 2)  
    elif (float(venta) > 2000):
        comision = round(float(venta) * 0.30, 2)
        sueldoTotal = sueldoBase + comision
        
    
    sueldoTotal = sueldoBase + comision
    sueldoTotal = round(sueldoTotal, 2)
    
    Label(ventana, text="Nombre", justify="center",
                 bg="#7D86B0", 
                 bd= "3",
                 fg ="black",
                 font= "Helvetica 11 bold",
                 padx= "3", 
                 pady ="3",  width="15",
                 relief = "ridge"
          ).place(x="100",y="290")
    
    Label(text=f"{nombre.get()}",bg="#B1B2C7", bd="3",
                padx= "3", 
                 pady ="3", 
                 relief = "ridge", justify="left",
                 fg ="black", width="15",
                 font= "helvetica 11").place(x="100",y="315")
    
    Label(ventana, text="Categoría", justify="center",
                 bg="#7D86B0", 
                 bd= "3",
                 fg ="black",
                 font= "Helvetica 11 bold",
                 padx= "3", 
                 pady ="3",  width="10",
                 relief = "ridge"
          ).place(x="230",y="290")
    
    Label(text=f"{categoría}",bg="#B1B2C7", bd="3",
                justify="left", padx= "3", 
                 pady ="3", relief = "ridge",
                 fg ="black",  width="10",
                 font= "helvetica 11" ).place(x="230", y="315") 
    
    Label(ventana, text="Sueldo Base", justify="center",
                 bg="#7D86B0", 
                 bd= "3",
                 fg ="black",
                 font= "Helvetica 11 bold",
                 pady ="3", padx= "3",  width="10",
                 relief = "ridge"
          ).place(x="329",y="290")
    
    Label(text=f" $ {sueldoBase}", bg="#B1B2C7", bd="3",
                 justify="right",padx= "3", 
                 pady ="3", relief = "ridge",
                 fg ="black",  width="10",
                 font= "helvetica 11" ).place(x="329", y="315")
    
    Label(ventana, text="Ventas", justify="center",
                 bg="#7D86B0", 
                 bd= "3",
                 fg ="black",
                 font= "Helvetica 11 bold",
                 padx= "3", pady ="3",  width="10",
                 relief = "ridge"
          ).place(x="428",y="290")
    
    Label(text=f"${venta}",bg="#B1B2C7", bd="3",
                 padx= "3", justify="right",
                 pady ="3", relief = "ridge",
                 fg ="black",  width="10",
                 font= "helvetica 11").place(x="428", y="315")
    
    Label(ventana, text="Comisión", justify="center",
                 bg="#7D86B0", 
                 bd= "3",
                 fg ="black",
                 font= "Helvetica 11 bold",
                 padx= "3", 
                 pady ="3",  width="10",
                 relief = "ridge"
          ).place(x="520",y="290")
    
    Label(text=f" ${comision}",bg="#B1B2C7", bd="3",
                 padx= "3", justify="right",
                 pady ="3", relief = "ridge",
                 fg ="black",  width="10",
                 font= "helvetica 11").place(x="520", y="315")
    
    Label(ventana, text="Sueldo Total", justify="center",
                 bg="#7D86B0", 
                 bd= "3",
                 fg ="black",
                 font= "Helvetica 11 bold",
                 padx= "3", 
                 pady ="3",  width="10",
                 relief = "ridge"
          ).place(x="615",y="290")
    
    Label(text=f" ${sueldoTotal}",bg="#B1B2C7", bd="3",
                 padx= "3", justify="right",
                 pady ="3", relief = "ridge",
                 fg ="black",  width="10",
                 font= "helvetica 11").place(x="615", y="315")
       
 
lbRotulo = Label(ventana,
                 text="CÁLCULO DE SUELDO MENSUAL",
                 bg="#7D86B0", 
                 bd= "7",
                 fg ="black",
                 font= "Helvetica 14 bold",
                 padx= "10", 
                 pady ="10", 
                 relief = "ridge" #"groove"                
)
lbRotulo.pack(padx="5", pady ="10")  #place(x="", y ="")


lbNombre = Label(ventana, 
                 text = "Ingrese el nombre del vendedor",
                 bg="#B1B2C7",
                 fg ="black",
                 font= "helvetica 11 ",
)
lbNombre.place(x="100", y="85")

txNombre = Entry(ventana,
                 font= "Helvetica 11",
                 textvariable=nombre)
txNombre.place(x="320", y="88")

lbVentas = Label(ventana, 
                 text = "Ingrese sus ventas mensuales",
                 bg="#B1B2C7",
                 fg ="black",
                 font= "helvetica 11 ",    
)
lbVentas.place(x="100", y="120")

txVentas = Entry(ventana, justify ="right",textvariable=ventas, font= "helvetica 11")
txVentas.place(x="320", y="120")

lbCategoría = Label(ventana, 
                 text = "Seleccione la categoría",
                 bg="#B1B2C7",
                 fg ="black",
                 font= "helvetica 11",   
)
lbCategoría.place(x="100", y="160")

cA = Radiobutton(ventana, text="A", value=1, bg="#B1B2C7", bd ="5", fg ="black",
                 font= "helvetica 11", variable=opcion)
cA.place(x="310", y="157")

cB = Radiobutton(ventana, text="B", value=2, bg="#B1B2C7", bd ="5", fg ="black",
                 font= "helvetica 11", variable=opcion)
cB.place(x="380", y="157")

cC = Radiobutton(ventana, text="C", value=3, bg="#B1B2C7", bd ="5",fg ="black",
                 font= "helvetica 11", variable=opcion)
cC.place(x="450", y="157")



b = Button(ventana, 
                  text ="Calcular",
                  background="#7D86B0", 
                  bd =5,
                  font= "Helvetica 11 bold",
                  command = mostrarDatos
                  )
b.place(x="100", y="210")


btCerrar = Button(ventana, 
                  text ="Cerrar la ventana",
                  background="#7D86B0", 
                  bd =5, 
                  font= "Helvetica 11",
                  command = ventana.destroy 
                  )
btCerrar.place(x="710", y="440")

ventana.mainloop()