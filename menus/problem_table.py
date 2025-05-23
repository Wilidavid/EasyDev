import variables as v
import table
import filters_script as filt
#name, link, diff, Vistas, resuelto, marcado favorito
import menus
from pynput import keyboard as kb
        

class make_table(menus.menu):
    def __init__(self, page=1, filters=[[filt.return_true, None]]*len(v.archivos[0]), limit_per_page=20):
        self.page=page
        self.filters=filters
        self.limit_per_page=limit_per_page
        self.archivos = [x[:4] + [len(x[y]) for y in range(4,6)]+ x[6:] for x in v.archivos]
        self.refresh()
        self.startlistening()
    def refresh(self):
        self.table = self.get_table()
        self.index=0
        self.show()
    def enter(self):
        pass # Since we already have the index and page we pretty much know the problem we selecting, all left is the function to click it
    def startlistening(self):
        with kb.Listener(self.listen) as escuchador:
            escuchador.join()
        return
    def down(self):
        self.index+= 1 
        if self.index>=len(self.table)-2:
            self.page+= 1 if ((self.page) * self.limit_per_page <= len(v.archivos)) else 0
            self.refresh()
        else:self.show()
        return True
    def up(self):
        self.index-= 1 
        if self.index<1 :
            self.page-=1 if self.page>0 else 0 
            self.refresh()
        else:self.show()
        return True
    def purge(self, element, num_element):
        return self.filters[num_element][0](element,self.filters[num_element][1])
    def get_table(self):
        elements = [x for x in self.archivos if all(self.purge( x[j], j) for j in range(len(self.filters)))][(self.page-1)*self.limit_per_page:(self.page)*self.limit_per_page]
        notable_stats=[[0, 'Nombre'],[2, 'Dificultad'],[3,'Vistas'],[4, '# Veces resuelto']]
        included = [x[0] for x in notable_stats]
        to_show = [[x[1] for x in notable_stats]] + [[str(x[y]) for y in included] for x in elements]

        return to_show
make_table(limit_per_page=10)