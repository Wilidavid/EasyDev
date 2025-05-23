import json
#link, diff, Vistas, resuelto, marcado favorito
x=[1,2,False]
print(x[0:20])
if True:
    cuentas = open('archivos.json')
    x=json.load(cuentas)
    for i in range(len(x)):
        x[i]=['pepe']+x[i][:2]+[0,[],[]]
    tosave=[[x,'archivos']]

    for todump, fname in tosave:
        try:
            hiii=json.dumps(todump)
        except:pass
        else:
            ola=open(f"{fname}.json","w")
            ola.write(hiii)
            ola.close()