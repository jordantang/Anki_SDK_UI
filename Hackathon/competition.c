#include <stdio.h>
#include <stdlib.h>
#include "SDK.h"

char* car_names[4];

int main (char* argv[], int argc) {
	
	FILE *move, pos1, pos2, pos3, pos4, posLast;
	int num_cars, energy*, i;
	ANKI_start();
	num_cars = argc - 1;
	energy = calloc(num_cars, sizeof(int));
	for(i = 1; i < argc - 1; i++) {
		
	}
	move = fopen("moves", r);

	ANKI_end();
}