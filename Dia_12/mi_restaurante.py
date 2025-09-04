from tkinter import *

aplicacion = Tk()

# pone tamaño y ubicación
aplicacion.geometry('1020x630+0+0')

aplicacion.resizable(0,0)

aplicacion.title("Mi restaurante - Sistema de facturación")

aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT, bg='burlywood')
panel_superior.pack(side=TOP,fill='x')

etiqueta_titulo = Label(panel_superior, text="Sistema de facturación", fg="azure4", font=('Arial',40),
                        bg='burlywood')
etiqueta_titulo.grid(row=0,column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo,text='Comidas', font=('Arial',15,'bold'), bd=1, relief=FLAT, bg='azure')
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo,text='Bebidas', font=('Arial',15,'bold'), bd=1, relief=FLAT, bg='azure')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo,text='Postres', font=('Arial',15,'bold'), bd=1, relief=FLAT, bg='azure')
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()



# evitar que la pantalla se cierre
aplicacion.mainloop()
