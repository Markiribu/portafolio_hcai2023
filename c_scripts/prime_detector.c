#include <stdio.h>

// es el numero n primo o no?, eso responde esta funcion
int is_prime(int n) {
  // por definicion un numero primo debe ser divisible solo por si mismo y 1, entonces si no es asi, return false(0)
  for (int i=2; i<=(n/2); i++) {
    if (n % i == 0) {
      return 0;
    }
  }

  return 1;
}

int main() {
  // array de numeros hasta el 200
  int primes[200];
  // cuenta del numero un indice en esencia
  int count = 0;

  // ciclo desde el 2 hasta el 200
  for (int i=2; i<=200; i++) {
    // en caso de ser un numero primo se añade al array
    if (is_prime(i)) {
      primes[count++] = i;
    }
  }

  // mostrando el array de numeros primos final
  for (int i=0; i<count; i++) {
    printf("%d ", primes[i]);
  }

  printf("\n");

  return 0;
}

