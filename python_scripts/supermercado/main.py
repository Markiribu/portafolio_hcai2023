#https://cruise.umple.org/umpleonline/umple.php?model=2310066gucw82vuhyz#genArea
class Persona():
    """Clase Persona describe a una persona generica, con items en el inventario y un dado tiempo en el universo"""
    def __init__(self):
        self.items = 0
        self.tlocal = 0

class Validador(Persona):
    """Clase Validador describe aquella persona que recibe un trabajo(validar) y lo ejecuta en un dado tiempo"""
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
    """Clase Cliente describe aquella persona que posee un set de items a buscar y luego entregar en caja para validar"""
    def __init__(self, buscfactor=200):
        self.buscfactor = buscfactor
        self.search_time = 0

    def set_target(self, nitems):
        self.items = nitems
        self.searchTime = nitems*self.buscfactor

    def buscar_items(self, dt):
        while(0 < dt and 0 < self.searchItem):
            self.searchTime -= 1
            dt -= 1
        return dt

    def comprar(self):
        return self.items

class Caja():
    """Clase Caja describe el conjunto validador y cola de clientes, en donde se le entrega el trabajo al validador respectivo al primer cliente en cola"""
    def __init__(self):
        self.cajero = Validador
        self.cola = []

    def add_cliente(self, Cliente):
        _added_client = self.cola.append(Cliente)

    def kick_client(self):
        _kicked_client = self.cola.pop(0)
        return 0

    def trabajar(self,dt):
        cliente_en_atencion = self.cola[0]
        self.cajero.get_items(cliente_en_atencion.items)
        dt = self.cajero.validar(dt)
        return dt

class Supermarket():
    """Clase Supermarket describe el conjunto de cajas, Clientes buscando elementos y los Clientes en total"""
    def __init__(self):
        self.cajas = []
        self.clientes_buscando = []
        self.clientesTotal = []

    def set_flujo(self,clientespordt):
        self.clientespordt = clientespordt
        return 0

    def __clientes_nuevos(self):
        for times in range(self.clientespordt):
            nuevo_cliente = Cliente()
            nuevo_cliente.settarget(15)
            self.clientes_buscando.append()
        return 0

    def __clientes_buscar(self, dt):
        while(0 < dt and not self.clientes_buscando):
            dt = cliente_buscando.buscar_items(dt)
            self.clientes_buscando.pop(0)
        return 0

    def __asignar_cajas(self):
        return 0

    def run(self):
        return 0

class Simulacion():
    """Clase principal genera un objeto tipo Supermarket y simula durante una cantidad de tiempo, luego entregara """
    def __init__(self, duration=86400):
        self.local = Supermarket
        self.duration = duration

    def correr_simulacion(self):
        return 0

#-------------------------------------------

print('Hermano se ve grandecito')
