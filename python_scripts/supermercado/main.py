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
    
    def __init__(self,buscfactor=200):
        self.buscfactor = buscfactor
        self.search_time = 0

    def set_target(nitems):
        self.items = nitems
        self.searchTIme = nitems*self.buscfactor

    def buscar_items(self, nitems):
        while(0 < dt and 0 < self.searchItem):
            self.searchTime -= 1
            dt -= 1
        return dt

    def comprar(self):
        return self.items

class Caja():
    def __init__(self):
        self.cajero = Validador
        self.cola = []

    def add_cliente(self, Cliente):
        self.cola.append(Cliente)

    def kick_client(self):
        return 0

    def trabajar(self):
        return 0

class Supermarket():
    def __init__(self):
        self.cajas = []
        self.clientes_buscando = []
        self.clientesTotal = []

    def set_flujo(cps):
        return 0

    def __clientes_nuevos():
        return 0

    def __clientes_buscar():
        return 0

    def __asignar_cajas():
        return 0

    def run():
        return 0

class Simulacion:
    def __init__(self):
        local = Supermarket

    def correr_simulacion():
        return 0

#-------------------------------------------

print('Hermano se ve grandecito')
