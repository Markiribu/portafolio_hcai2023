#include <stdio.h>

// Definiendo arrays y recorriendolo
int main(){
	int basic_array[10];
	for (int i=0; i<10; i++) {
		basic_array[i] = i*2;
	}
	for (int i=0; i<10; i++) {
		printf("counter[%d] = %d\n ", i, basic_array[i]);
	}
	return 0;
}
