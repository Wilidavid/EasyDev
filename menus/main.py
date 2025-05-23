import os 
from getpass import getpass as gp
import variables as v
import json
import menus
def prints(a):
    print(a)
def inputs(a):
    print()
    return input(a)

def login():
    input()
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
    input()
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

def close_terminal():exit()
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
    opt=[['Iniciar sesion', login], ['Registrarse', register], ['Salir', close_terminal]]
    while True:
        menus.menu(opt=opt,name='Menu principal')




def menu():
    os.system('cls')
    prints('Bienvenido al programa, que desea hacer')
    for b, a in  enumerate(v.opciones):
        prints(f'{b+1}. {a[0]}') #Imprimir el nombre de la opcion
    input()

main_menu()