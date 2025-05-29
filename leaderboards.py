import variables as v
import table as tt
def get_sorted(favorites):
    key=[lambda x: len(x[5]),lambda x: x[8][1]][not favorites]
    return [['     '+str(ix+1)+ '     ', str(x[0]),str( len(x[5]) if favorites else x[8][1])]  for ix, x in  enumerate(sorted([[i] + v.cuentas[i] for i in v.cuentas.keys()],reverse=True,key=key))]
def leaderboard(favorites, num=15):
    table = get_sorted(favorites=favorites)
    elements = [['#', 'Usuario', '# De '+ str('Problemas hechos' if favorites else 'Racha')] ]+ table[:num]
    if v.usuario_actual not in [x[1] for x in elements]:
        elements.append(["..."]*3)
        ff = [ix for ix, x in enumerate(table) if x[1]==v.usuario_actual][0]
        elements.append(table[ff])
    tt.show(elements=elements)