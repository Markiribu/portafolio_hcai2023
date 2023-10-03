# Clase 12: Definiendo clases, compactando y manejando
### Los objetos, mas especificamente las clases pueden pedir en un dado orden los atributos a asignar al objeto, 
### -----------------
#### from dataclasses import dataclass
#### @dataclass
#### class Estudiantes:
#### 	nombre: str
#### 	RUT: str
#### 	edad: int
#### 	nivel: int
#### 
#### est = Estudiantes('Testsubject', '12.345.678-9', 25, 4)
#### est.RUT
### ---------------------------
### A la hora de herencia de metodos, podemos tener polimorfismo
