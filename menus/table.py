tabla=[ 
       ["Nombre", "Ocupacion", "Años", "hermanos", "var"],
       ["Pedro", "ingeniero", "5", "1", "ph1"],
       ["Wilson","Desempleado", "NO", "2", "ph2"],
       ["bosdfdsfdsfsdscvfdfscdvfdsb","muerto","600", "3", "ph3"],
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
def show(elements, selectedcord, skip=None):
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
    
    skipping= (skip!=None)
    
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
        if skipping and ix2 in skip or not skipping: print(c[bordercolor]+line)
def prepare(problem=None, profile_name=None, selected=-1, favorited=False, done=False):
    datafavorite="89"
    datadone="1223"
    visitas="100"
    description = """Lorem ipsum dolor sit amet, consectetur 
    adipiscing elit. In mattis nunc vel condimentum aliquam. Praesent 
    
    facilisis et mauris sit amet ultrices. Fusce faucibus tincidunt eros, quis posuere leo feugiat a. Nunc efficitur diam eu arcu maximus, non molestie justo rutrum. In efficitur elementum tellus, ut
    cursus purus tincidunt in. Donec eleifend felis ex, sed tincidunt urna molestie quis. Maecenas eget nisl interdum quam viverra tristique. Vestibulum a ex hendrerit, auctor leo sed, scelerisque tortor. In maxi
    mus, sapien vel tristique mollis, arcu dolor placerat felis, at viverra nisl lectus id erat. Duis at purus justo. Vestibulum sed tincidunt felis. Suspendisse in magna sit amet mi sodales viverra at eleifend orci.
    Curabitur at bibendum risus, quis convallis leo.Donec ornare viverra orci ut ullamcorper. Proin mollis ipsum sit amet ipsum porttitor, a laoreet libero maximus. Vestibulum sit amet libero eu dui tincidunt aliquet ac
    cumsan a magna. Etiam laoreet ex eu dolor aliquet fermentum. Ut sodales odio ultrices elit semper, non sollicitudin sapien malesuada. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis
    egesta
    s. Maecenas 
    placerat ex vitae mauris sagittis, eu ornare metus mollis. Vestibulum laoreet mauris in bibendum lobortis. Ut interdum nec nibh eget efficitur.Nam non interdum arcu, at tempor sapien. Etiam at ullamcorper justo. In nec vehicula tellus, id lobortis mi. Duis ac dolor faucibus, egestas ex sed, volutpat dolor. Nam fermentum velit felis, in convallis risus finibus eget. Praesent molestie mattis lorem, eu facilisis leo gravida quis. Integer fringilla, felis nec tempor elementum, neque diam pretium est, non dapibus augue nisi nec mi. Morbi id volutpat elit, vitae faucibus mi. Vestibulum fringilla elit quis arcu hendrerit, non ullamcorper elit mattis.""" #Define description here
    name = "el problema con tu madre"
    linelength = 85
    words = description.split()
    lines=[""]
    ix = 0
    c=0
    
    for i in words:
        c+=len(i)+1
        if c>=linelength:
           lines.append("")
           c=len(i)+1
           ix+=1
        lines[ix]+=i+" "
    tabla = [["Nombre:", name, "#"]]
    for ixx,i in enumerate(lines):
        txt = "Descripcion/Vistas:" if ixx == (len(lines))//2 else ""
        txt2 = visitas if ixx == (len(lines))//2 else ""
        tabla.append([txt, i, txt2])
    lenn = len(lines)
    skip = [0, lenn, lenn+1, lenn+2]
    tabla.append(["Marcado como hecho: ", str(done), datadone])
    tabla.append(["Marcado como favorito:", str(favorited), datafavorite])
    show(elements=tabla,selectedcord=selected,skip=skip)

            
     
    


