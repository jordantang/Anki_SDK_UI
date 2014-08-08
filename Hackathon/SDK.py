import socket
import signal
import sys
import subprocess
import os
import time
import errno

sock = -1       # Store the socket to the server process
server = -1     # Store the server process
car_list = []   # Store all the cars known in the list

logfile = 'SDK.log'     # Filename for the logfile

# ----- USER FUNCTIONS ----- #
# Start session with SDK
#  Call this before starting any program
def ANKI_start():
  # Clear and start the debug log
  clear_file(logfile);

  # Kill server and vehicle tools/scans in the background
  DEVNULL = open(os.devnull, 'w')
  subprocess.call("sudo killall server", shell=True, 
                    stdout=DEVNULL, stderr=DEVNULL)
  subprocess.call("sudo killall vehicle-tool", shell=True,
                    stdout=DEVNULL, stderr=DEVNULL)
  subprocess.call("sudo killall vehicle-scan", shell=True,
                    stdout=DEVNULL, stderr=DEVNULL)
  DEVNULL.close()

  # Spawn server in background process
  global server
  server = subprocess.Popen(['./server/server'])

  # Check to see if the server was opened correctly
  if (server.pid < 0):
    msg = ('Error in spawning server')
    print msg
    write_file(logfile, msg)
    return

  # Add a signal handler to kill process on various signals
  signal.signal(signal.SIGTERM, sig_handler);
  signal.signal(signal.SIGINT, sig_handler);
  signal.signal(signal.SIGSEGV, sig_handler);

  # Wait until the server starts accepting calls or the timeout occurs
  time.sleep(3)
  global car_list
  car_list = (open('vehicle_scan_file').readlines())

# Sends a certain roadmap to the car (currently only oval_track is loaded into the SDK)
#   The roadmap is necessary if you want to change tracks of the car and read back
#   position data.  By default, all cars are sent the roadmap of the starter kit map.
# Parameters:
#   ncar - name of the car
#   roadmap - name of the roadmap
# Returns:
#   -1  - if an error occurs
#    0  - otherwise
def send_roadmap(ncar, roadmap):
  parse = 0

  # Create message
  wr = '/write_roadmap/'
  if (ncar == 'all'):
    wr = '/write_roadmap'
    car = ''
  else:
    car = get_car_id(ncar)
    if (car == 'not found'):
      logbuf = 'send_roadmap: Could not find desired car ' + ncar 
      write_file(logfile, 'send_roadmap: Could not find desired car ' + ncar)
      print logbuf
  szData = wr + car + '/' + str(roadmap) 

  # Send roadmap msg to the server
  reply = send_msg(szData)
  # Get parse reply
  if (parse_reply(reply) < 0):
    parse = -1

  msg = 'RETURN CODE: ' + str(parse)
  write_file(logfile, msg)
  return parse
 
# Sends the starting position to the car
#   We can't tell where we are to start with, so the user needs to send this down
# Parameters:
#   ncar - name of the car
#   offset - offset from the center of the road in mm
# Returns:
#   -1  - if an error occurs
#    0  - otherwise
def send_start_position(ncar, offset):
  # Get the car name
  wr = '/write/'
  car = ''
  if (ncar == 'all'):
    wr = '/write_all'
  else:
    car = get_car_id(ncar)
    if (car == 'not found'):
      logbuf = 'set_offset: Could not find desired car ' + ncar
      write_file(logfile, logbuf)
      print logbuf
      return -1
  szData = wr + car + '/' + offset
  reply = send_msg(szData)
  
  if (parse_reply(reply) < 0):
    return -1
  return 0

# Scans for unconnected nearby cars and returns the list
# Parameters: timeout - time to scan the cars for
# Returns:
#   list of unconnected nearby cars, empty if an error occurs
def scan_cars(timeout):
  # Send a message to the server to rescan for the cars
  szData = '/rescan/' + str(timeout) + '/'
  reply = send_msg(szData)
  if (parse_reply(reply) < 0):
    return ''
  return (open('vehicle_scan_file').readlines())

# Connect to a car given the name of the car and which bluetooth device to use
#  If no bluetooth device is chosen, the connection will default to hci0
#  Parameters:
#    car - name of the car you wish to connect to
#  Returns:
#    -1 - if an error has occured
#     0 - if the connection was made correctly
def connect_car(ncar):
  err = 0
  # Get the car mac address from id
  car = get_car_id(ncar)

  # Rescan for the car if it isn't found
  if (car == 'not found'):
    rescan_cars(5)
    car = get_car_id(ncar)
    # Could not find car in scan, so it's either off or not close enough to adapter
    if (car == 'not found'):
      logbuf = 'connect_car: Could not connect to car because not found in scan'
      write_file(logfile, logbuf)
      print logbuf
      return -1
  else:
    # Rescan to whitelist ble adapter
    rescan_cars(1)

  # Send the message to the server
  szData = '/connect/'+ car 
  reply = send_msg(szData)
  
  # Parse the reply message to get return code
  if (parse_reply(reply) < 0):
    err = -1

  # Send the default roadmap to the car
  szData = '/write_roadmap/' + car
  send_msg(szData)
  
  # Parse the reply message to get return code
  if (parse_reply(reply) < 0):
    err = -1

  # Send the sdk-mode-off to the car
  szData = '/write/' + car + '/sdk_mode_off'
  send_msg(szData)

  # Parse the reply message to get return code
  if (parse_reply(reply) < 0):
    err = -1
  
  return err

# Set the light pattern on a car
#  Parameters: 
#    ncar - name of the car you wish to send the message to
#    channel - select from "RED", "TAIL", "BLUE", "GREEN", "FRONTL", "FRONTR"
#    effects - select from "STEADY", "FADE", "THROB", "FLASH", "RANDOM"
#    start - how many seconds should it take before the cycle begins
#    end - how many seconds should the cycle last for
#    cycles_per_minute - how many times should the cycle occurs per minute
#  Returns:
#    -1 - if an error has occured
#     0 - if the message was correctly sent to the car
def set_lights(ncar, channel, effect, start, end, cycles_per_minute):
  # Set parse return code
  parse = 0    

  # Lookup the corresponding index to channel and effect
  ichannels = ["RED", "TAIL", "BLUE", "GREEN", "FRONTL", "FRONTR"]
  ieffects =  ["STEADY", "FADE", "THROB", "FLASH", "RANDOM"]

  # Check car
  wr = '/write/'
  if (ncar == 'all'):
    wr = '/write_all'
    car = ''
  else:
    car = get_car_id(ncar)
    if (car == 'not found'):
      logbuf = 'set_lights: Could not find desired car ' + ncar
      write_file(logfile, logbuf)
      print logbuf
      return
  
  # Create message
  szData = wr + car + '/set_light_pattern/' 
  for x in range(0, len(ichannels)):
    if (ichannels[x] == channel.upper()):
      szData = szData + str(x)
  szData = szData + '/'
  for x in range(0, len(ieffects)):
    if (ieffects[x] == effect.upper()):
      szData = szData + str(x)
  szData = szData + '/' + str(start) +'/' + str(end) +'/'+ str(cycles_per_minute)
 
  # Create and send message to server
  reply = send_msg(szData)
  
  # Send return code back to user
  if (parse_reply(reply) < 0):
    parse = -1
  msg = 'RETURN CODE: ' + str(parse)
  write_file(logfile, msg)

  return parse

# Set the speed for the motors
#  Parameters:
#    ncar - name of the car you want to connect to
#    speed - speed for the motors to reach
#    accel - acceleration for the motors to ramp up to speed
#  Returns:
#    -1 - if an error has occured
#     0 - if a message was correctly sent to the car
def set_speed(ncar, speed, accel):
  global sock
  parse = 0

  # Create message
  wr = '/write/'
  if (ncar == 'all'):
    wr = '/write_all'
    car = ''
  else:
    car = get_car_id(ncar)
    if (car == 'not found'):
      logbuf = 'set_speed: Could not find desired car ' + ncar
      write_file(logfile, logbuf)
      print logbuf
      return
  szData = wr + car + '/set_speed/' + str(speed) + '/' + str(accel)
  
  # Send set speed msg to the server
  reply = send_msg(szData)
  # Get parse reply
  if (parse_reply(reply) < 0):
    parse = -1

  msg = 'RETURN CODE: ' + str(parse) 
  write_file(logfile, msg)
  return parse 

# Change the lane of the car
#  Parameters: 
#    ncar - name of the car you wish to connect to (or "all" to send the msg to all cars)
#    speed - speed for the car to move at
#    lane - lane that the car should move to (based on the starting position of the car)
#  Returns:
#    -1 - if an error has occured
#     0 - if a message was correctly sent to the car
def change_lane(ncar, speed, lane):
  global sock
  # Create the message
  wr = '/write/'
  if (ncar == 'all'):
    wr = '/write_all'
    car = ''  
  else:
    car = get_car_id(ncar)
    if (car == 'not found'):
      logbuf = 'change_lane: Could not find desired car ' + ncar
      write_file(logfile, logbuf)
      print logbuf
      return

  # Store result from reply of server
  parse = 0

  # Send change lane car message
  szData = wr + car + '/change_lane/' + str(speed) + '/' + str(lane*10.0) + '/'
  reply = send_msg(szData)
  
  # Add the two parse replies together
  if (parse_reply(reply) < 0):
    parse = -1 

  msg = 'RETURN CODE: ' + str(parse)
  write_file(logfile, msg)

  return parse

# Disconnect to a car given the name of the car and which bluetooth device to use
# You do not need to disconnect from a car before exiting your program
#  This function is only useful if you want to remove a car midway through the program
#  Parameters:
#    ncar - name of the car you wish to connect to
#  Returns:
#    -1 - if an error has occured
#     0 - if the connection was made correctly
def disconnect_car(ncar):
  car = get_car_id(ncar)
  if (car == 'not found'):
    logbuf = 'disconnect_car: Could not find desired car ' + ncar
    write_file(logfile, logbuf)
    print logbuf
    return -1
  szData = '/write/disconnect/' + car + '/' + adapter
  reply = send_msg(szData)

  if (parse_reply(reply) > 0):
    return 0
  return -1

# End session with the SDK
#  Call this before ending any program.  Automatically disconnects from all cars.
def ANKI_end():
  global server
 
  # Send the server a SIGTERM to kill it 
  if (server.poll() == None):
    os.kill(server.pid, signal.SIGTERM)
    os.waitpid(server.pid, 0)

# ----- UTIL FUNCTIONS ----- #
# Catch a signal so the program exits
def sig_handler(signal, frame):
  ANKI_end()

# Send a message to the server
def send_msg(szData):
  global sock

  # Open the socket to send the message
  sock_open()

  #Send some data to remote server
  message = "GET " + szData + " HTTP/1.1\r\n\r\n"
 
  try :
    #Set the whole string
    sock.sendall(message)
  except socket.error:
    #Send failed
    msg = 'send_msg: Send failed on msg' + message
    write_file(logfile, msg)
    return ''
 
  write_file(logfile, 'send_msg: Message sent:')
  write_file(logfile, message)

  # Get return reply from the server
  reply = sock.recv(1024)
  write_file(logfile, reply)

  # Close the socket to the server
  sock_close()

  # Send the msg back
  return reply

# Parse reply to get return code from server
#   Return code from server
def parse_reply(reply):
  # Look for colon in reply (return code is right after colon)
  try :
    index = reply.index(':')
  except ValueError:
    write_file(logfile, 'Could not find _:_ in message to return error code')
    return -1

  if ((index +1) > len(reply)):
    write_file(logfile, 'Could not find return code in return message')
    return -1
  return reply[index+1:len(reply)]

# Check the socket to the server
def sock_open():
  # Create an AF_INET, STREAM socket (TCP)
  global sock
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  HOST = 'localhost'     # connection to server locally
  SERVER_PORT = 2500     # server at port 2500

  try:
    # Connect to spawned server process
    sock.connect((HOST, SERVER_PORT))
    write_file(logfile, 'sock_open: Socket Created')
    return 0
  except socket.error, msg:
    return -1

# Close the socket to the server
def sock_close():
  global sock
  sock.close()
  write_file(logfile, 'sock_close: Closed socket');

# Write to the file
def write_file(filename, szData):
  fLog = open(filename, "a")
  fLog.write(szData)
  fLog.write("\n")
  fLog.close

# Clear the file
def clear_file(filename):
  fLog = open(filename, "w+")
  fLog.write("")
  fLog.close

# Parse the car name from each line
def get_car_name_from_line(szData):
  # Move over to the start past the MAC address length
  MACADDR_len = 17
  start = MACADDR_len+1
  end = szData.index('[')-1
  logbuf = 'get_car_name_from_line: Writing substring to file from index ' + str(start) + ' to ' + str(end)
  write_file(logfile, logbuf)
  logbuf = 'get_car_name_from_line: Found substring of ' + szData[start:end]
  write_file(logfile, logbuf)
  return szData[start:end]

# Gets the id of the car given the name of the car
#   Parameters:
#     name - name of the car
#   Returns:
#     car id               - if found in scan
#     'not found'          - if car could not be found in the scan
def get_car_id(name):
  global car_list
  # Look for the car id in the car list
  write_file(logfile, 'get_car_id: Got lines:')
  for x in car_list:
    logbuf = 'get_car_id: ' + x
    write_file(logfile, logbuf)
    # Parse each line for the name of the car
    car_line = get_car_name_from_line(x)
    if (car_line == name):
      # If the car was found in the list, return the mac addr (car id)
      MACADDR_len = 17
      logbuf = 'get_car_id: Found car ' + name + ' [' + x[:(MACADDR_len)] + ']'
      write_file(logfile, logbuf)
      return x[:(MACADDR_len)]
  return 'not found'

# Scans for nearby cars
# Parameters: timeout - time to rescan the cars for
# Returns:
#   -1  - if an error occurs
#    0  - otherwise
def rescan_cars(timeout):
  # Send a message to the server to rescan for the cars
  szData = '/rescan/' + str(timeout) + '/'
  reply = send_msg(szData)
  if (parse_reply(reply) < 0):
    return -1
  return 0
