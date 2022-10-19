from functools import total_ordering
import tkinter as Tk

from setuptools import sic

# Funciones
def domicilio():
    if z.get() == 1:
        precioenv = 1.50
        envio = "Si"
        return precioenv, envio
    else:
        precioenv = 0
        envio = "No"
        return precioenv, envio

def bebida():
    if y.get() == 1:
        precio = 0.75
        orden = "gaseosa"
        return precio, orden
    elif y.get() == 2:
        precio = 0.60
        orden = "chocolate caliente"
        return precio, orden
    elif y.get() == 3:
        precio = 0.50
        orden = "Refresco natural"
        return precio, orden

def pupusas():
    preciobev, tipobev = bebida()
    precioenv, envio = domicilio()
    cant = int(cantidad.get())
    if x.get() == 1:
        tipo = "queso"
        precio = 0.70
        totalord = precio * cant
        total = totalord + preciobev + precioenv
        
        print("Pupusas de: " + tipo + " Cantidad: " + str(cant) + "  Total: $" + str(totalord) +
        "\nBebida: " + tipobev + "  Total: $" + str(preciobev) + "\nEnvio:  " + envio + "   Total: $" + str(precioenv) +
        "\nTotal: $" + str(total))
    elif x.get() == 2:
        tipo = "frijol con queso"
        precio = 0.65
        totalord = precio * cant
        total = totalord + precioenv + preciobev
        print("Pupusas de: " + tipo + " Cantidad: " + str(cant) + "  Total: $" + str(totalord) +
        "\nBebida: " + tipobev + "  Total: $" + str(preciobev) + "\nEnvio:  " + envio + "   Total: $" + str(precioenv) +
        "\nTotal: $" + str(total))
    elif x.get() == 3: 
        tipo = "Revuelta"
        precio = 0.6
        totalord = precio * cant
        total = totalord + precioenv + preciobev
        print("Pupusas de: " + tipo + " Cantidad: " + str(cant) + "  Total: $" + str(totalord) +
        "\nBebida: " + tipobev + "  Total: $" + str(preciobev) + "\nEnvio:  " + envio + "   Total: $" + str(precioenv) +
        "\nTotal: $" + str(total))



#configuracion de la ventana
ventana = Tk.Tk()
ventana.geometry("700x500")

x = Tk.IntVar()
y = Tk.IntVar()
z = Tk.IntVar()

#elementos del tkinter

#Labels
titulo = Tk.Label(ventana, text="pupuseria la cabra")
lb1 = Tk.Label(ventana, text="Especialiades de pupusas")
lb2 = Tk.Label(ventana, text="Bebidas")
lb3 = Tk.Label(ventana, text="¿A domicilio?")
lb4 = Tk.Label(ventana, text="Cantidad: ")

# Imagenes
lbqueso = Tk.Label(ventana, text="pupusa de queso")
lbfq = Tk.Label(ventana, text="pupusa de frijol con queso")
lbrev = Tk.Label(ventana, text="pupusa revueta")
lbgas = Tk.Label(ventana, text="caseosa")
lbchoc = Tk.Label(ventana, text="chocolate caliente")
lbref = Tk.Label(ventana, text="refresco")

#Botones
btn1 = Tk.Button(ventana, text="imprimir factura", width=30, command=pupusas)

#RadioButtons
rb1 = Tk.Radiobutton(ventana, text="Queso", value=1, variable=x)
rb2 = Tk.Radiobutton(ventana, text="Frijol con queso", value=2, variable=x)
rb3 = Tk.Radiobutton(ventana, text="Revueltas", value=3, variable=x)
rb4 = Tk.Radiobutton(ventana, text="Gaseosa", value=1, variable=y)
rb5 = Tk.Radiobutton(ventana, text="Chocolate", value=2, variable=y)
rb6 = Tk.Radiobutton(ventana, text="Refresco", value=3, variable=y)
rb7 = Tk.Radiobutton(ventana, text="Si", value=1, variable=z)
rb8 = Tk.Radiobutton(ventana, text="No", value=2, variable=z)

#entry
cantidad = Tk.Entry(ventana)

#posicion de los elementos
titulo.place(relx=0, rely=0)
lb1.place(relx=0.3, rely=0.1)
lb2.place(relx=0.32, rely=0.5)
lb3.place(relx=0.1, rely=0.85)
lb4.place(relx=0.7, rely=0.35)

cantidad.place(relx=0.8, rely=0.35)

#imagenes
lbqueso.place(relx=0.1, rely=0.25)
lbfq.place(relx=0.3, rely=0.25)
lbrev.place(relx=0.55, rely=0.25)
lbgas.place(relx=0.1, rely=0.6)
lbchoc.place(relx=0.3, rely=0.6)
lbref.place(relx=0.55, rely=0.6)

#radiobuttons
rb1.place(relx=0.1, rely=0.35)
rb2.place(relx=0.3, rely=0.35)
rb3.place(relx=0.55, rely=0.35)

rb4.place(relx=0.1, rely=0.7)
rb5.place(relx=0.3, rely=0.7)
rb6.place(relx=0.55, rely=0.7)

rb7.place(relx=0.3, rely=0.85)
rb8.place(relx=0.4, rely=0.85)

btn1.place(relx=0.5,rely=0.85)
ventana.mainloop()