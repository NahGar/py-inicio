import os

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido,numero_cuenta,balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} Nº cta: {self.numero_cuenta} Saldo: {self.balance}"

    def depositar(self, monto):
        self.balance += monto
        print("Depósito efectuado")

    def retirar(self, monto):
        if self.balance < monto:
            print(f"Fondos insuficientes ({self.balance})")
            input("Presiones cualquier tecla")
        else:
            self.balance -= monto
            print("Retiro efectuado")

def elegir_menu():
    print("[1] - depositar")
    print("[2] - retirar")
    print("[3] - salir")
    while True:
        opcion = input("Elige una opción:")
        if opcion.isdigit() and int(opcion) >= 1 and int(opcion) <= 3:
            return int(opcion)
        else:
            print("Opción incorrecta")

def ingresar_monto():
    while True:
        print("Ingrese el monto ")
        monto = input()
        if monto.isdigit():
            return int(monto)
        else:
            print("Monto incorrecto")

def crear_cliente():
    nombre = ""
    apellido = ""
    cuenta = ""
    balance = ""

    while True:
        if nombre == "":
            print("Ingrese su nombre: ")
            nombre = input()
        if apellido == "":
            print("Ingrese su apellido: ")
            apellido = input()
        if cuenta == "":
            print("Ingrese su número de cuenta: ")
            cuenta = input()
        #if balance == "":
        #    print("Ingrese su balance: ")
        #    balance = input()
        if not cuenta.isdigit():
            print("Cuenta incorrecta, debe ser numérica")
            cuenta = ""
        # if not balance.isdigit():
        #    print("Balance incorrecto, debe ser numérica")
        #    balance = ""
        if nombre != "" and apellido != "" and cuenta != "":  #and balance != "":
            #cliente = Cliente(nombre,apellido,int(cuenta),int(balance))
            cliente = Cliente(nombre, apellido, int(cuenta))
            return cliente


def inicio():

    cliente = crear_cliente()

    salir = False
    while salir == False:
        os.system("cls")
        print("-" * 50)
        print("Bienvenido al sistema bancario")
        print("-" * 50)
        print(cliente)

        opcionMenu = elegir_menu()
        match opcionMenu:
            case 1:
                monto = ingresar_monto()
                cliente.depositar(monto)
            case 2:
                monto = ingresar_monto()
                cliente.retirar(monto)
            case 3:
                print("Bye!")
                salir = True


inicio()
