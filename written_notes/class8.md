# Punteros repaso de clase 7
## Es posible asignar memoria dinamica a un dado array, obtienes optimizacion en tener los valores del array de manera adjacente en memoria
### int \*counter;
### int Nele = 5;
### // malloc reserva memoria
### counter = malloc(Nele\*sizeof(int));
### // Ahora counter[\*] se puede usar igual a un array estatico
### for (int i=0; i<Nele;i++)
### 	counter[i] = i;
### // Luego de usar, la memoria dinámica se debe liberar:
### free(counter);
# Makefile Make, automatiza y compila tu proyecto de un socataz
## Tiene la siguiente estructura en donde al no ser cumplido el objetivo ejecutara lo identado siempre y cuando las condiciones/dependencias si esten cumplidas
### objetivo : condiciones
### 	$(COMANDOS EN BASH)
## Esto tiene el potencial de compilar grandes proyectos con multiples dependencias sin la necesidad de correr todos los comandos encesarios uno por uno.
## make -j(numero) para "compilar" utilizando multiples hilos.
