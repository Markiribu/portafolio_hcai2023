class Fraccion():
    def __init__(self, numerador, denominador):
        self.n = numerador
        self.d = denominador
    def __rep__(self):
        self.print = str(n) + '' + str(d)

x = Fraccion(1,2)

print(x.n,'/',x.d)
print(x)
