from pynput import keyboard as kb
import table

def si():return True
class menu():
    def up(self):
        self.index-= 1 if self.index>=1 else 0
        self.show()
        return True
    def down(self):
        self.index+= 1 if self.index<len(self.table)-2 else 0
        self.show()
        return True
    def enter(self):
        self.args =self.opt[self.index][2] if self.args else []
        self.run=self.functs[self.index]
        return False
    def listen(self, key):
        keys=self.keys
        if key in keys.keys(): 
            g=keys[key]()
            return [False if key in [kb.Key.enter, kb.Key.left,kb.Key.esc] else g][0]
        

    def __init__(self, opt, name, args=False):
        self.keys = {kb.Key.up: self.up,kb.Key.down: self.down ,kb.Key.enter:self.enter}
        self.args = args
        self.opt = opt
        self.name=name
        self.functs = [x[1] for x in self.opt]
        self.table = [[name]] + [[x[0]] for x in self.opt]
        
        self.index=0
        
        self.show()
        with kb.Listener(self.listen) as escuchador:
            escuchador.join()
        self.rt=self.run(*self.args)
        return
    def show(self):
       table.show(elements=self.table,selectedcord=self.index+1)
        

    



