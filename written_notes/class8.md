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
# Makefile Make, y compilar tu proyecto de un socataz!
# 
