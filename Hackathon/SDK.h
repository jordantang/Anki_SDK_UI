#include <stdio.h>

// Start session with SDK
//  Call this before starting any program
void ANKI_start();

// Scans for nearby cars
//  If no bluetooth adapter is chosen, the connection will default to hci0
//  Parameters:
//    timeout - length of time to scan cars for
//    adapter - bluetooth adapter that you wish to scan with
void scan_cars(char *adapter, int timeout);

// Connect to a car given the name of the car and which bluetooth device to use
//  If no bluetooth device is chosen, the connection will default to hci0
//  Parameters:
//    car - mac address of the car you wish to connect to
//    adapter - bluetooth adapter that you wish to use fo the connection
//  Returns:
//    -1 - if an error has occured
//     0 - if the connection was made correctly
int connect_car(char *car, char *adapter);

// Set the light pattern on the cars
//  Parameters: 
//    car - the car you wish to send the message to
//    channel - select from "RED", "TAIL", "BLUE", "GREEN", "FRONTL", "FRONTR"
//    effects - select from "STEADY", "FADE", "THROB", "FLASH", "RANDOM"
//    start - how many seconds should it take before the cycle begins
//    end - how many seconds should the cycle last for
//    cycles_per_minute - how many times should the cycle occurs per minute
//  Returns:
//    -1 - if an error has occured
//     0 - if the message was correctly sent to the car
int set_lights(char *car, char *channel, char *effects, unsigned int start, unsigned int end, unsigned int cycles_per_minute);

// Set the speed for the motors
//  Parameters:
//    speed - speed for the motors to reach
//    accel - acceleration for the motors to ramp up to speed
//  Returns:
//    -1 - if an error has occured
//     0 - if a message was correctly sent to the car
int set_speed(char *car, unsigned int speed, int accel);

// Change the lane of the car
//  Parameters: 
//    car - mac address of the car you wish to connect to (or "all" to send the msg to all cars)
//    speed - speed for the car to move at
//    lane - lane that the car should move to (based on the starting position of the car)
//  Returns:
//    -1 - if an error has occured
//     0 - if a message was correctly sent to the car
int change_lane(char *car, unsigned int speed, int lane);

// Disconnect to a car given the name of the car and which bluetooth device to use
//  If no bluetooth device is chosen, the connection will default to hci0
//  Parameters:
//    car - mac address of the car you wish to connect to
//    adapter - bluetooth adapter that you wish to use fo the connection
//  Returns:
//    -1 - if an error has occured
//     0 - if the connection was made correctly
int disconnect_car(char *car);

// End session with the SDK
//  Call this before ending any program.  Automatically disconnects from all cars.
//  Parameters: - session number to the server socket to close (return from ANKI_start)
void ANKI_end(); 
