import socket
import sys
import subprocess
import time

sock = -1       # Store the socket to the server process
server = -1     # Store the pid of the server process

# Start session with SDK
#  Call this before starting any program
def ANKI_start():
  # Spawn server in background process
  global server
  server = subprocess.Popen("./server/server &", shell=True).pid

  # Check to see if the server was opened correctly
  if (server < 0):
    print('Error in spawning server')
    return
  
  time.sleep(5);
  # Bind the socket to an address
  global sock
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind(('', 5001))     # bind the socket to port 5001  

  # Connect to spawned server process
  HOST = ''              # local host
  CLIENT_PORT = 5001     # client at port 5001
  SERVER_PORT = 2500     # server at port 2500
  #sock.create_connection((HOST, CLIENT_PORT), (HOST,SERVER_PORT))
  sock.connect((HOST, SERVER_PORT))

# Send message to cars
def 

# Scans for nearby cars
#  If no bluetooth adapter is chosen, the connection will default to hci0
#  Parameters:
#    timeout - length of time to scan cars for
#    adapter - bluetooth adapter that you wish to scan with
def scan_cars(adapter, timeout):
  pass

# Connect to a car given the name of the car and which bluetooth device to use
#  If no bluetooth device is chosen, the connection will default to hci0
#  Parameters:
#    car - mac address of the car you wish to connect to
#    adapter - bluetooth adapter that you wish to use fo the connection
#  Returns:
#    -1 - if an error has occured
#     0 - if the connection was made correctly
def connect_car(car, adapter):
  pass

# Set the light pattern on the cars
#  Parameters: 
#    car - the car you wish to send the message to
#    channel - select from "RED", "TAIL", "BLUE", "GREEN", "FRONTL", "FRONTR"
#    effects - select from "STEADY", "FADE", "THROB", "FLASH", "RANDOM"
#    start - how many seconds should it take before the cycle begins
#    end - how many seconds should the cycle last for
#    cycles_per_minute - how many times should the cycle occurs per minute
#  Returns:
#    -1 - if an error has occured
#     0 - if the message was correctly sent to the car
def set_lights(car, channel, effect, start, end, cycles_per_minute):
  pass

# Set the speed for the motors
#  Parameters:
#    speed - speed for the motors to reach
#    accel - acceleration for the motors to ramp up to speed
#  Returns:
#    -1 - if an error has occured
#     0 - if a message was correctly sent to the car
def set_speed(car, speed, accel):
  pass

# Change the lane of the car
#  Parameters: 
#    car - mac address of the car you wish to connect to (or "all" to send the msg to all cars)
#    speed - speed for the car to move at
#    lane - lane that the car should move to (based on the starting position of the car)
#  Returns:
#    -1 - if an error has occured
#     0 - if a message was correctly sent to the car
def change_lane(car, speed, lane):
  pass

# Disconnect to a car given the name of the car and which bluetooth device to use
#  If no bluetooth device is chosen, the connection will default to hci0
#  Parameters:
#    car - mac address of the car you wish to connect to
#    adapter - bluetooth adapter that you wish to use fo the connection
#  Returns:
#    -1 - if an error has occured
#     0 - if the connection was made correctly
def disconnect_car(car):
  pass

# End session with the SDK
#  Call this before ending any program.  Automatically disconnects from all cars.
def ANKI_end():
  # Send the server a SIGTERM to kill it
  global server
  os.kill(server, 15)
 
  # Close the socket connection to the server
  global s
  s.close()


