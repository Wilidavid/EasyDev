import table
import variables as v
import menus
from pynput import keyboard as kb 
from database import database2 as db 
from guardar import guardar
def returnfalse(): return False
class problem_view_menu(menus.menu):
    def __init__(self, id, ix=-1, p=True):
        self.keys = {kb.Key.up: self.up,kb.Key.down: self.down ,kb.Key.enter:self.enter}
        self.functs = [self.marcar_hecho,self.marcar_favorito, returnfalse]
        
        self.index=ix
        self.id=id
        self.problem=v.archivos[id]
        if p:v.archivos[id][3]+=1
        self.table = self.prepare()
        if self.index==-1:self.index=self.skip[2]
        self.show()
        
        with kb.Listener(self.listen) as escuchador:
            escuchador.join()
        self.rt=self.run(*self.args)
        return 
    

    def marcar_favorito(self):
        if self.problem[-1] not in v.cuentas[v.usuario_actual][5]:
            v.cuentas[v.usuario_actual][5].append(self.problem[-1])
            v.archivos[self.problem[-1]][5].append(v.usuario_actual)
        else:
            v.cuentas[v.usuario_actual][5].remove(self.problem[-1])
            v.archivos[self.problem[-1]][5].remove(v.usuario_actual)

        db.change_usuario(v.usuario_actual,v.cuentas[v.usuario_actual])
        return guardar()

    def marcar_hecho(self):
        if self.problem[-1] not in v.cuentas[v.usuario_actual][4]:
            v.cuentas[v.usuario_actual][4].append(self.problem[-1])
            v.archivos[self.problem[-1]][4].append(v.usuario_actual)
        else:
            v.cuentas[v.usuario_actual][4].remove(self.problem[-1])
            v.archivos[self.problem[-1]][4].remove(v.usuario_actual)
            
        db.change_usuario(v.usuario_actual,v.cuentas[v.usuario_actual])
        return guardar()
    


    def enter(self):
        self.args =[]
        self.run=self.functs[self.index-self.skip[2]]
        return False
    def up(self):
        self.index-= 1 if self.index>=self.skip[3] else 0
        self.show()
        return True
    def down(self):
        self.index+= 1 if self.index<len(self.table)-1 else 0
        self.show()
        #print(self.index,len(self.table))
        return True
    def repeat(self):
        problem_view_menu(id=self.id, ix = self.index)

    def prepare(self):
        problem=self.problem
        done,favorited = [v.usuario_actual in x for x in problem[4:6]]
        datafavorite=len(problem[5])
        datadone=len(problem[4])
        visitas=problem[3]
        description = problem[6]
        name = problem[0]
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
        lines.append(f'LINK: {problem[1]}')
        lines.append(f'Dificultad: {v.translator[problem[2]]}')
        tabla = [["Nombre:", str(name), "#"]]
        for ixx,i in enumerate(lines):
            txt = "Descripcion/Vistas:" if ixx == (len(lines))//2 else ""
            txt2 = visitas if ixx == (len(lines))//2 else ""
            tabla.append([str(txt), str(i), str(txt2)])
        lenn = len(lines)
        self.skip = [0, lenn, lenn+1, lenn+2, lenn+3]
        tabla.append(["Marcado como hecho: ", str(done), str(datadone)])
        tabla.append(["Marcado como favorito:", str(favorited), str(datafavorite)])
        tabla.append(["----------", 'Volver', '----------'])
        return tabla
    def show(self):
        return table.show(elements=self.table,selectedcord=self.index,skip=self.skip)
