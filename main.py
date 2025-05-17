import os 
from getpass import getpass as gp
import variables as v
import json
def prints(a):
    print(a)
def inputs(a):
    print()
    return input(a)
def login():
    os.system('cls')
    contra=None
    usuario='default'
    while v.cuentas[usuario][0]!=contra:
        os.system('cls')
        usuario=inputs('Por favor digite su usuario, ingrese "Volver" para volver al menu de inicio: ')
        if usuario.lower() == 'volver':return False
        contra=gp('Por favor digite la contraseña: ')
        
        if usuario not in v.cuentas.keys():
            usuario='default'
            contra='asd'
    v.usuario_actual=usuario
    return True
def register():
    os.system('cls')
    usuario=inputs('Por favor digite el usuario de la cuenta que quiere crear, digite "Volver" para volver al menu de inicio: ')
    if usuario == 'volver':return False
    contraseña=inputs('Por favor ingrese la contraseña que su nueva cuenta va a tener: ')
    if usuario in v.cuentas.keys():
        return False
    v.cuentas[usuario]=[contraseña]
    v.usuario_actual=usuario
    guardar()
    return True

def guardar():
    tosave=[[v.cuentas,'cuentas'], [v.archivos,'archivos']]
    for todump, fname in tosave:
        try:
            hiii=json.dumps(todump)
        except:pass
        else:
            ola=open(f"{fname}.json","w")
            ola.write(hiii)
            ola.close()
def main_menu():
    opt=[['Iniciar sesion', login], ['Registrarse', register]]
    while True:
        os.system('cls')
        prints('Bienvenido a el programa.')    
        for ix, x in enumerate(opt):
            prints(f'{ix+1}. {x[0]}')
        try:
            op =int(input())-1
            if opt[op][1]():
                menu()
        except:pass

def menu():
    os.system('cls')
    prints('Bienvenido al programa, que desea hacer')
    for b, a in  enumerate(v.opciones):
        prints(f'{b+1}. {a[0]}') #Imprimir el nombre de la opcion
    input()

main_menu()