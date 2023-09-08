#include <stdio.h>
#define linux_system 1

/* un programa basico que solo molesta con define y los ifdef */
int main()
{
#ifdef linux_system
	printf("Soy un sistema basado en linux!");
#elif windows_system
	printf("Soy un sistema windows";)
#elif mac_system
	printf("Soy un sistema mac!");
#endif
	return 0;
}
