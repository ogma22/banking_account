from random import randint
import os

#Clases
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Nombre cliente: {self.nombre} {self.apellido}\nNúmero de cuenta: {self.numero_cuenta}\nBalance: ${self.balance}'

    def depositar(self):
        deposito = input ('\nDigite el valor del depósito:\n')
        while deposito.isdigit() == True and int(deposito) > 0:
            balance = int(self.balance)
            balance += int(deposito)
            print(f'Se ha realizado un depósito por ${deposito}\n')
            return balance

    def retirar(self):
        retiro = input('\nDigite el valor del retiro:\n')
        while retiro.isdigit() == True and int(retiro) > 0:
            balance = int(self.balance)
            if balance - int(retiro) >= 0:
                balance -= int(retiro)
                print(f'Se ha realizado un retiro por ${retiro}\n')
            else:
                print('\nFondos insuficientes')
            return balance

#Funciones propias del código
def consultar_cliente(entr):
    os.chdir('C:\\Diana\\Diana2023\\Data Science\\Python\\16_days\\Day 7\\Cuentas')
    count = 0
    with open('registro.txt') as file:
        ret = 'NE', 0, 0, 0
        for line in file:
            if count > 0:
                l = line.split(',')
                cliente = Cliente(l[0], l[1], l[2], l[3])
                if cliente.numero_cuenta == entr:
                    ret = cliente
                    return 1, ret
            count += 1
        return 0, ret

def pedir_cuenta():
    while True:
        opcion = input('\nSelecciona una opción:\n'
              '[1] Ingresar con número de cuenta\n'
              '[2] Abrir una cuenta nueva\n'
              '[3] Salir\n')
        if opcion != '1' and opcion != '2' and opcion != '3':
            print('Opción inválida')
        elif int(opcion) == 1:
            ret = input('Ingresa el número de cuenta\n')
            return ret
        elif int(opcion) == 3:
            return 'finalizar'
        else:
            return 'crear'

def crear_cliente():
    nombre = input('Ingresa tu nombre:\n')
    apellido = input('Ingresa tu apellido:\n')
    coincidencias_cuenta = 1
    while coincidencias_cuenta == 1:
        cuenta = randint(0, 99999999)
        numero_cuenta = str(cuenta)
        with open('registro.txt') as file:
            for line in file:
                coincidencias_cuenta = 0
                if numero_cuenta in line:
                    coincidencias_cuenta += 1
                    break

    cliente = Cliente(nombre, apellido, numero_cuenta,'0')
    linea = f'\n{nombre},{apellido},{numero_cuenta},0'
    file = open('registro.txt','a')
    file.write(linea)
    file.close()
    print(f'Se ha abierto una nueva cuenta para el '
          f'titular {nombre} {apellido} con número {cuenta}\n')

def menu():
    while True:
        opcion = input('\nSelecciona una opción:\n'
                       '[1] Depositar dinero\n'
                       '[2] Retirar dinero\n'
                       '[3] Salir\n')
        if opcion != '1' and opcion != '2' and opcion != '3':
            print('Opción inválida')
        elif opcion == '1':
            return 'depositar'
        elif opcion == '2':
            return 'retirar'
        else:
            return 'finalizar'

def actualizar_balance(nombre, apellido, cuenta, balance):
    with open('registro.txt') as file:
        count = 0
        while True:
            linea = file.readline()
            count += 1
            if cuenta in linea:
                linea = f'{nombre},{apellido},{cuenta},{balance}\n'
                file.close()
                break
        with open('registro.txt') as file:
            lines = file.readlines()
            lines[count-1] = linea
            with open ('registro.txt', 'w') as file:
                for line in lines:
                    file.write(line)

def finalizar():
    print('Gracias por preferirnos.\nBanco OGMA22')

print('Bienvenido')
while True:
    entrada = pedir_cuenta()
    if entrada == 'crear':
        crear_cliente()
    elif entrada == 'finalizar':
        break
    else:
       existe, cliente = consultar_cliente(entrada)
       if existe == 0:
           print('Este cliente no existe\n')
       else:
           opcion = menu()
           if opcion == 'depositar':
                cliente.balance = cliente.depositar()
                actualizar_balance(cliente.nombre,cliente.apellido, cliente.numero_cuenta,cliente.balance)
                print(cliente)
           elif opcion == 'retirar':
               cliente.balance = cliente.retirar()
               actualizar_balance(cliente.nombre, cliente.apellido, cliente.numero_cuenta, cliente.balance)
               print(cliente)
           else:
               break
finalizar()
