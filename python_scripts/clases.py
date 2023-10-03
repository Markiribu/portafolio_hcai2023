class Fraccion():
    def __init__(self, n, d):
        """ El primer argumento sera el numerador y el segundo el denominador, deben ser ambos enteros """
        if ((type(n)!=int) ^ (type(d)!=int)):
            raise Exception("ERROR: numerador y denominador deben ser numeros enteros")
        self.n = n
        self.d = d
    
    def simplificar(self):
        """Simplifica la fraccion lo maximo posible, no acepta argumentos"""
        if ((self.n < self.d) & (self.d%self.n == 0) & (self.n != 1)):
            self.d /= self.n
            self.n /= self.n
        if ((self.d < self.n) & (self.n%self.d == 0) & (self.d != 1)):
            self.n /= self.d
            self.d /= self.d
        self.d = int(self.d)
        self.n = int(self.n)
    
    def __str__(self):
        """ La representacion de la fraccion es tal que "numerador/denominador" """
        return(str(self.n)+"/"+str(self.d))

    def __add__(self, c):
        """ La suma entre fracciones es directa dependiendo de si los denominadores son iguales o no """
        if c.d == self.d:
            resultado = Fraccion(self.n+c.n,self.d)
            resultado.simplificar
            return(resultado)
        else:
            resultado = Fraccion(((self.n*c.d)+(c.n*self.d)),self.d*c.d)
            resultado.simplificar
            return(resultado)
    
    def __mul__(self, c):
        """ La multiplicacion es directa, numerador por numerador y denominador por denominador y luego se simplifica el resultado """
        resultado = Fraccion(self.n*c.n,self.d*c.d)
        resultado.simplificar
        return(resultado)

x = Fraccion(10,9)
x2 = Fraccion(11,9)
x3 = Fraccion(12,10)


print(x*x2)
