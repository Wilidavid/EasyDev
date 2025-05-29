import variables as v
import datetime as dt
from dateutil import relativedelta

def savedate():
    f=v.cuentas[v.usuario_actual][7][0]
    if f!='':
        rp = int(calctime(v.cuentas[v.usuario_actual][7][0]))
        print(rp)
        if rp==0:
            v.cuentas[v.usuario_actual][7][1]=0
        elif rp==1:
            v.cuentas[v.usuario_actual][7][1]+=1
    print(v.cuentas[v.usuario_actual])
    v.cuentas[v.usuario_actual][7][0]=str(dt.datetime.now().date())

def calctime(dt1):
    diff =relativedelta.relativedelta(dt.datetime.strptime(dt1, "%Y-%m-%d"), dt.datetime.strptime(str(dt.datetime.now().date()), "%Y-%m-%d"))
    return 0 if abs(diff.days)>1 or abs(diff.months)>0 else str(1 if abs(diff.days)==1 else 2)
