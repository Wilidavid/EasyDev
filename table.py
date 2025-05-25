
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
            

            traits=["fin"]
            if ix2== selectedcord: traits+=[selectedcolor, "negrilla"]
            if ix2== 0: traits+=[main_color, "negrilla"]
            

            traitsfinal = [c[trait] for trait in traits]
            for i in traitsfinal:print(i,end="")

            print(f"{it}", end=c[bordercolor]+"|")
        print()
        if skipping and ix2 in skip or not skipping: print(c[bordercolor]+line)




            
     
    


