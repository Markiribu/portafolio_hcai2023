#https://cruise.umple.org/umpleonline/umple.php?model=2310066gucw82vuhyz#genArea
class Persona():
    def __init__(self):
        self.items = 0
        self.tlocal = 0

class Validador(Persona):

    def __init__(self, fac=5):
        self.validfactor = fac
        self.validationTime = 0

    def get_items(self, nitems):
        self.items = nitems
        self.validationTime = nitems*self.validfactor

    def validar(self, dt):
        while(0 < dt and 0 < self.validationTime):
            self.validationTime -= 1
            dt -= 1
        return dt

class Cliente(Persona):
    
    def __init__(self):
        self.buscfactor = 0
        self.search_time = 0
