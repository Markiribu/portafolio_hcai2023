# Clase 17: La importancia del dato
## Puntos de los datos
* Almacenamiento
Como guardaras el dato, de que manera se pueden mantener al futuro.
* Composicion
El tipo de dato, numerico/categorico, relacional/no-relacional, homogeneo/heterogeneo, 
* Tamaño
Bytes
* Comunicacion
Quien es tu publico objetivo, como se leera[Idealmente un formato similar a los catalogos de illustris]
* Escalamiento
Determinar si los datos son estaticos o se modificaran con el tiempo.[Mis datos o calculos tienden una tendencia a ser dependientes]
## Almacenamiento en texto plano
CSV, TXT, tienden a ser mas sencillos de abrir y utilizar.
en pyton el escribir flush, o close ayuda a guardar y escribir un archivo.
	archivo.close() #cierra el archivo y guarda al almacenamiento
	archivo.flush() #mantiene abierto el archivo y guarda al almacenamiento
Recordar que uno abre un archivo con archivo.open(nombre, metodo), en donde el metodo puede ser read-only o write.

