#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "SDK.h"
#define TURNS 5
#define MAX_COMMAND_LEN 80

char** car_names;

int main (int argc, char* argv[]) {
	
	FILE *move, pos1, pos2, pos3, pos4, posLast, scan;
	int num_cars, energy*, i, j;
	char *command[MAX_COMMAND_LEN];
	ANKI_start();
	num_cars = argc - 1;
	energy = calloc(num_cars, sizeof(int));
	car_names = calloc(num_cars, sizeof(char*));
	//Setup for car names, connection, and files
	scan_cars("", 5);
	scan = fopen("scanfile", r);

	//Change in order to parse for mac address in file
	for(i = 1; i < argc - 1; i++) {
		connect_car(argv[i], "");
		strcpy(car_names[i-1], argv[i]);
	}
	move = fopen("moves", r);
	posLast = fopen("posLast", w);

	//Gameplay here
	for(i = 0; i < TURNS; i++) {
		for(j = 0; j < num_cars; j++) {
			system(car_names[i]);
		}
		fgets(command, MAX_COMMAND_LEN, move);
		
	}
	ANKI_end();
}