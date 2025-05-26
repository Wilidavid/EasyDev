import variables as v
import table
import filters_script as filt
import menus
import problem_view
from pynput import keyboard as kb
def returnfalse():return False
class make_table(menus.menu):
    def __init__(self, page=1, limit_per_page=10, just_the_table=False):
        self.page=page
        self.paraaa=False
        self.keys = {kb.Key.up: self.up,kb.Key.down: self.down ,kb.Key.enter:self.enter, kb.Key.left:self.go_back,kb.Key.esc:self.go_back}
        self.limit_per_page=limit_per_page
        self.order=v.cuentas[v.usuario_actual][3][0]
        self.index=0
        self.refresh()
        if not just_the_table:
            self.startlistening()
        else:
            return 
        return
    

    def refresh(self):
        self.archivos = sorted( [x[:2]+[v.translator[x[2]]] +  x[3:4] + [len(x[y]) for y in range(4,6)]+ x[6:] + [' ♥ ' if x[-1] in v.cuentas[v.usuario_actual][5] else '   '] for x in v.archivos], key = lambda x:x[self.order], reverse=v.cuentas[v.usuario_actual][3][1])
        self.table = self.get_table()
    def go_back(self):
        self.paraaa=True
        return False
    def enter(self):
        return False
    def startlistening(self):
        while True:
            self.refresh()
            self.show()
            with kb.Listener(self.listen) as escuchador:
                escuchador.join()
            if not self.paraaa:
                while problem_view.problem_view_menu(id=self.get_id()).rt:pass
            else:break
        return False
    
    def down(self):
        self.index+= 1 
        if self.index>=len(self.table)-1:
            self.page+= 1 if (((self.page) * self.limit_per_page ) + self.index <= len(v.archivos)-1) else 0
            self.refresh()
            self.index=0
            self.show()
            
        else:self.show()
        return True
    def up(self):
        self.index-= 1 
        if self.index<0 :
            self.page-=1 if self.page>1 else 0 
            self.refresh()
            self.index=self.limit_per_page-1
            self.show()
        else:self.show()
        return True
    def purge(self, element, num_element, id):
        match num_element:
            case 2:
                return (element == v.translator[v.cuentas[v.usuario_actual][1]]) or (v.cuentas[v.usuario_actual][1]==-1)
            case 4:
                x=id in v.cuentas[v.usuario_actual][4]
                match v.cuentas[v.usuario_actual][2]:
                    case 0:return not x
                    case 1:return True
                    case 2:return x
            case 5:
                x=id in v.cuentas[v.usuario_actual][5]
                match v.cuentas[v.usuario_actual][6]:
                    case 1:return not x
                    case 0:return True
                    case 2:return x
            case _:       
                    return True 
    def get_id(self):
        return self.elements[self.index][8]
    def get_table(self):
        self.elements_raw = [x for x in self.archivos if all(self.purge( x[j], j, x[7]) for j in range(len(x)))]
        self.elements=[[ix+1] + x  for ix,x  in enumerate(self.elements_raw)][(self.page-1)*self.limit_per_page:(self.page)*self.limit_per_page]
        notable_stats=[[0, '#'],[1, 'Nombre'],[2, 'Link'],[3, 'Dificultad'],[4,'Vistas'],[5, '# Veces resuelto'], [9, ' ']]
        included =  [x[0] for x in notable_stats]
        to_show = [[x[1] for x in notable_stats]] + [[str(x[y]) for y in included] for x in self.elements]
        return to_show
