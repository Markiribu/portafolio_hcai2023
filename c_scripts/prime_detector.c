#include <stdio.h>

// A function to check if a number is prime
int is_prime(int n) {
  // A prime number is divisible only by itself and 1
  for (int i = 2; i <= n / 2; i++) {
    if (n % i == 0) {
      return 0;
    }
  }

  return 1;
}

int main() {
  // Initialize an array to store the prime numbers
  int primes[200];
  int count = 0;

  // Iterate through all numbers from 2 to 200
  for (int i = 2; i <= 200; i++) {
    // If the number is prime, add it to the array
    if (is_prime(i)) {
      primes[count++] = i;
    }
  }

  // Print the prime numbers
  for (int i = 0; i < count; i++) {
    printf("%d ", primes[i]);
  }

  printf("\n");

  return 0;
}

