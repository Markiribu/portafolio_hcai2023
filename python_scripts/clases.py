class Fraccion():
    def __init__(self, numerador, denominador):
        if ((type(numerador)!=int) ^ (type(denominador)!=int)):
            raise Exception("ERROR: numerador y denominador deben ser numeros enteros")
        self.n = numerador
        self.d = denominador
    def show(self):
        print(str(self.n)+'/'+str(self.d))

x = Fraccion(1,2)

x.show()
