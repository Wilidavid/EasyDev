tabla=[ 
       ["Nombre", "Ocupacion", "Años", "hermanos", "var"],
       ["Pedro", "ingeniero", "5", "1", "ph1"],
       ["Wilson","Desempleado", "NO", "2", "ph2"],
       ["Simonbolivardelagrandetrinidad","muerto","600", "3", "ph3"],
       ["Hola", "Muy bien", "69", "0", "ph4"],
       ["Hola2", "Muy bien2", "692", "02", "ph4"]
       ]
import os
c={
    "princ" : '\033[95m',
    "azul" : '\033[94m',
    "cyan" : '\033[96m',
    "verde" : '\033[92m',
    "amarillo" : '\033[93m',
    "rojo" : '\033[91m',
    "fin" : '\033[0m',
    "negrilla" : '\033[1m',
    "subrayado":'\033[4m'
    }
def show(elements, selectedcord):
    os.system("cls")
    print("\n."*5)
    
    bordercolor="azul"
    selectedcolor="amarillo"
    main_color="cyan"

    elements2 = [[x[y] for x in elements] for y in range(len(elements[0]))]
    maxl = [max([len(str(y)) for y in x]) for x in elements2]
    slines = sum(maxl)
    lside = slines + len(elements2) + 1
    lside2 = (2* len(elements)) + 1
    line = lside * "="
    
    print(c[bordercolor]+line)
    for ix2, i in enumerate(elements):
        print(f"{c[bordercolor]}|", end=c["fin"])
        for ix, j in enumerate(i):
            k = (maxl[ix] - len(j))
            spaces = " "*(k//2)
            it = spaces + j + spaces + (" " if k%2!=0 else "")
            
            
            ###ACA DEFINIMOS LAS REGLAS DE COLORACION A COLUMNAS
            traits=["fin"]
            if ix2== selectedcord: traits+=[selectedcolor, "negrilla"]
            if ix2== 0: traits+=[main_color, "negrilla"]
            
            ####### IMPREIMIMOS LA COLORACION
            traitsfinal = [c[trait] for trait in traits]
            for i in traitsfinal:print(i,end="")
            #######Imprimimos la linea
            print(f"{it}", end=c[bordercolor]+"|")
        print()
        print(c[bordercolor]+line)
    print("\n"*5)
cpp=1
show(tabla, cpp)
while True:
    cpp += [1, -1][(input()!="u")]
    show(tabla, cpp)