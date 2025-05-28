import json
x=[1,2,False]
print(x[0:20])
if True:
    cuentas = open('cuentas.json')
    x=json.load(cuentas)
    for i in x.keys():
        x[i].append([0,True])
    tosave=[[x,'cuentas']]

    for todump, fname in tosave:
        try:
            hiii=json.dumps(todump)
        except:pass
        else:
            ola=open(f"{fname}.json","w")
            ola.write(hiii)
            ola.close()