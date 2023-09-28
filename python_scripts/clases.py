class Fraccion():
    def __init__(self, numerador, denominador):
        if ((type(numerador)!=int) ^ (type(denominador)!=int)):
            raise Exception("ERROR: numerador y denominador deben ser numeros enteros")
        self.numerador = numerador
        self.denominador = denominador
    def show(self):
        print(str(self.numerador)+'/'+str(self.denominador))
    def simplificar(self):
        if self.numerador < self.denominador:
            while (((self.denominador%self.numerador) == 0) & (self.numerador != 1)):
                self.denominador /= self.numerador
                self.numerador /= self.numerador
        if ((self.denominador < self.numerador) & (self.denominador != 1)):
            self.numerador /= self.denominador
            self.denominador /= self.denominador
        self.denominador = int(self.denominador)
        self.numerador = int(self.numerador)

x = Fraccion(8,16)

x.simplificar()
x.show()
