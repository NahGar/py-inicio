from tkinter import *

aplicacion = Tk()

# pone tamaño y ubicación
aplicacion.geometry('1065x470+0+0')

aplicacion.resizable(0,0)

aplicacion.title("Mi restaurante - Sistema de facturación")

aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT, bg='burlywood')
panel_superior.pack(side=TOP,fill='x')

etiqueta_titulo = Label(panel_superior, text="Sistema de facturación", fg="azure4", font=('Arial',40),
                        bg='burlywood', padx=200)
etiqueta_titulo.grid(row=0,column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=55)
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

lista_comidas = ['pollo','cordero','asado','salmón','merluza','pizza','kebab','hamburguesa']
lista_bebidas = ['pepsi','cerveza','vino','coca-cola','fanta','sprite','whisky','7up']
lista_postres = ['isla flotante','chajá','pepas','flan','ricardito','helado','torta helada','pastel']

# para almacenar los valores de los checkboxes
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # crear checkbuttos
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Arial',15,'bold'), onvalue=1, offvalue=0,
                         variable=variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W)

    # crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, font=('Arial',15,'bold'),bd=1,width=6,state=DISABLED,
                                     textvariable=texto_comida[contador] ,justify=RIGHT)
    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1

# para almacenar los valores de los checkboxes
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    # crear checkbuttos
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Arial',15,'bold'), onvalue=1, offvalue=0,
                         variable=variables_bebida[contador])
    bebida.grid(row=contador, column=0, sticky=W)

    # crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, font=('Arial', 15, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_bebida[contador], justify=RIGHT)
    cuadros_bebida[contador].grid(row=contador, column=1)

    contador += 1

# para almacenar los valores de los checkboxes
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    # crear checkbuttos
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Arial',15,'bold'), onvalue=1, offvalue=0,
                         variable=variables_postre[contador])
    postre.grid(row=contador, column=0, sticky=W)

    # crear cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres, font=('Arial', 15, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_postre[contador], justify=RIGHT)
    cuadros_postre[contador].grid(row=contador, column=1)

    contador += 1

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos, text='Costo comida', font=('Arial',12,'bold'), bg='azure4', fg='white')
etiqueta_costo_comida.grid(row=0,column=0)

texto_costo_comida = Entry(panel_costos, font=('Arial',12,'bold'), bd=1, width=10, state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1, padx=41)

# etiquetas de costo y campos de entrada
etiqueta_costo_bebida = Label(panel_costos, text='Costo bebida', font=('Arial',12,'bold'), bg='azure4', fg='white')
etiqueta_costo_bebida.grid(row=1,column=0)

texto_costo_bebida = Entry(panel_costos, font=('Arial',12,'bold'), bd=1, width=10, state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1, padx=41)

# etiquetas de costo y campos de entrada
etiqueta_costo_bebida = Label(panel_costos, text='Costo bebida', font=('Arial',12,'bold'), bg='azure4', fg='white')
etiqueta_costo_bebida.grid(row=0,column=0)

texto_costo_bebida = Entry(panel_costos, font=('Arial',12,'bold'), bd=1, width=10, state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=2,column=1, padx=41)

# etiquetas de costo y campos de entrada
etiqueta_costo_postre = Label(panel_costos, text='Costo postre', font=('Arial',12,'bold'), bg='azure4', fg='white')
etiqueta_costo_postre.grid(row=2,column=0)

texto_costo_postre = Entry(panel_costos, font=('Arial',12,'bold'), bd=1, width=10, state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2,column=1, padx=41)

# etiquetas de costo y campos de entrada
etiqueta_subtotal = Label(panel_costos, text='Subtotal', font=('Arial',12,'bold'), bg='azure4', fg='white')
etiqueta_subtotal.grid(row=0,column=2)

texto_subtotal = Entry(panel_costos, font=('Arial',12,'bold'), bd=1, width=10, state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3, padx=41)

# etiquetas de costo y campos de entrada
etiqueta_impuesto = Label(panel_costos, text='Impuesto', font=('Arial',12,'bold'), bg='azure4', fg='white')
etiqueta_impuesto.grid(row=1,column=2)

texto_impuesto = Entry(panel_costos, font=('Arial',12,'bold'), bd=1, width=10, state='readonly',
                           textvariable=var_impuesto)
texto_impuesto.grid(row=1,column=3, padx=41)

# etiquetas de costo y campos de entrada
etiqueta_total = Label(panel_costos, text='Total', font=('Arial',12,'bold'), bg='azure4', fg='white')
etiqueta_total.grid(row=2,column=2)

texto_total = Entry(panel_costos, font=('Arial',12,'bold'), bd=1, width=10, state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2,column=3, padx=41)

# botones
botones = ['total','recibo','guardar','reiniciar']
columnas = 0
for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=('Arial',12,'bold'), fg='white', bg='azure4', bd=1, width=9)
    boton.grid(row=0,column=columnas)
    columnas += 1

# area recibo
texto_recibo = Text(panel_recibo, font=('Arial',12,'bold'), bd=1, width=42, height=10)
texto_recibo.grid(row=0,column=0)



# evitar que la pantalla se cierre
aplicacion.mainloop()
