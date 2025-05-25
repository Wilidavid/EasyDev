import variables as v
import json
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
    return True