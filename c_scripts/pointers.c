#include <stdio.h>

int main() {
	int var=10;
	int *pvar;

	pvar = &var;
	scanf("%d \n", &var);

	printf("var:%d \n",var);
	printf("&var:%ls \n",&var);
}
