import os 
from getpass import getpass as gp
import variables as v
import json
import menus
import problem_table
import problem_view
import random
from guardar import guardar


def login():
    input()
    os.system('cls')
    contra=None
    usuario='default'
    while v.cuentas[usuario][0]!=contra:
        os.system('cls')
        usuario=input('Por favor digite su usuario, ingrese "Volver" para volver al menu de inicio: ')
        if usuario.lower() == 'volver':
            main_menu()
            return
        contra=gp('Por favor digite la contraseña: ')
        
        if usuario not in v.cuentas.keys():
            usuario='default'
            contra='asd'
    v.usuario_actual=usuario
    menu()


def register():
    input()
    os.system('cls')
    usuario=input('Por favor digite el usuario de la cuenta que quiere crear, digite "Volver" para volver al menu de inicio: ')
    if usuario == 'volver':return False
    contraseña=input('Por favor ingrese la contraseña que su nueva cuenta va a tener: ')
    if usuario in v.cuentas.keys():
        main_menu()
        return False
    v.cuentas[usuario]=[contraseña,-1,0,[0,True], [], [], 0 ]
    v.usuario_actual=usuario
    guardar()
    menu()

def close_terminal():quit()






def admon():
    v.usuario_actual='a'
    menu()

def main_menu():
    opt=[['Iniciar sesion', login], ['Registrarse', register],['Admin login', admon], ['Salir', quit]]
    menus.menu(opt=opt,name='Ingreso de Datos')

def change_order_callback(n, b):
    v.cuentas[v.usuario_actual][3]=[n,b]
    guardar()
    change_order()

def change_order_types(n):
    on=[['Ascendente',change_order_callback, [n, True]], ['Descendente',change_order_callback, [n, False]], ['Volver',change_order, []]]
    menus.menu(name='Tipo de orden', opt=on, args=True)

def change_order():
    oporden = [['Ordenar por nombre', change_order_types, [0]],['Ordenar por link',change_order_types, [1]],   ['Ordenar por veces visto',change_order_types, [3]], ['Ordenar por veces favorito', change_order_types, [4]], ['Volver', config_filter, []]]
    menus.menu(opt=oporden,name='Ajustar orden', args=True)

def problemas_hechos_callback(n):
    v.cuentas[v.usuario_actual][2]=n
    guardar()
    config_filter()

def problemas_favoritos_callback(n):
    v.cuentas[v.usuario_actual][6]=n
    guardar()
    config_filter()

def dificultad_callback(n):
    v.cuentas[v.usuario_actual][1]=n
    guardar()
    config_filter()

    

def def_difficultad():
    opt=[ ['Facil', dificultad_callback, [0]],['Medio', dificultad_callback, [1]],['Dificil', dificultad_callback, [2]],['Avanzado', dificultad_callback, [3]],['Mostrar todos los problemas', dificultad_callback, [-1]],['Volver', config_filter, []] ]
    menus.menu(opt=opt,name='Elije el tipo de dificultad de los problemas que deseas filtrar', args=True)

def problemas_hechos():
    ph=[['Mostrar problemas hechos', problemas_hechos_callback, [1]], ['Ocultar problemas Hechos', problemas_hechos_callback, [0]], ['Mostrar SOLO problemas hechos', problemas_hechos_callback, [2]], ['Volver',menu]]
    menus.menu(opt=ph, name='Ajustar filtro de problemas ya hechos',args=True)
def favoritos_hechos():
    ph=[['Mostrar problemas favoritos', problemas_favoritos_callback, [0]], ['Ocultar problemas favoritos', problemas_favoritos_callback, [1]], ['Mostrar SOLO problemas favoritos', problemas_favoritos_callback, [2]], ['Volver',menu]]
    menus.menu(opt=ph, name='Ajustar filtro de problemas favoritos',args=True)


def wipeout_filters():
    v.cuentas[v.usuario_actual][1]=-1
    v.cuentas[v.usuario_actual][2]=0
    v.cuentas[v.usuario_actual][3]=[0,True]
    v.cuentas[v.usuario_actual][6]=0
    guardar()
    config_filter()

def wipe_warning():
    opt = [['Si', wipeout_filters], ['No', config_filter]]
    menus.menu(opt=opt, name='Estas seguro de que quieres hacer esto?')

def config_filter():
    optfiltro = [['Ajustar orden de aparicion de los problemas',change_order],['Problemas Hechos', problemas_hechos],['Problemas Favoritos',favoritos_hechos], ['Dificultad de los problemas', def_difficultad], ['Restablecer configuracion', wipe_warning], ['Volver', menu]]
    menus.menu(opt=optfiltro, name='Ajustar el filtro de los problemas')

def call_back_opt():
    opt=[['Ajustar filtro de problemas', config_filter], ['Volver', menu]]
    menus.menu(opt=opt,name=f'Ajustes de {v.usuario_actual}')



def problemos():
    problem_table.make_table()
    guardar()
    menu()


def random_problem():
    f = problem_table.make_table(just_the_table=True).elements_raw
    id= f[random.randint(0,len(f)-1)][7]
    problem_view.problem_view_menu(id)
    menu()


def menu():
    os.system('cls')
    opt=[['Lista de problemas',problemos],['Problema Aleatorio', random_problem], ['Opciones de cuenta', call_back_opt],['Salir', exit]]
    while True:menus.menu(opt=opt,name='Menu principal')

main_menu()