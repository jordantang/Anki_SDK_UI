import socket
import signal
import sys
import subprocess
import os
import time
import errno

sock = -1       # Store the socket to the server process
server = -1     # Store the server process
scan = -1       # Store the scan process

# ----- USER FUNCTIONS ----- #
# Start session with SDK
#  Call this before starting any program
def ANKI_start():
  # Start the debug log
  log_clear()

  # Spawn server in background process
  global server
  server = subprocess.Popen(['./server/server'])

  # Check to see if the server was opened correctly
  if (server.pid < 0):
    msg = ('Error in spawning server')
    print msg
    log_write(msg)
    return
 
  # Launch scan to clear bluetooth adapter
  scan_cars('', 1)

  # Add a signal handler to kill process on various signals
  signal.signal(signal.SIGTERM, sig_handler);
  signal.signal(signal.SIGINT, sig_handler);
  signal.signal(signal.SIGSEGV, sig_handler);
  
# Scans for nearby cars
#  If no bluetooth adapter is chosen, the connection will default to hci0
#  Parameters:
#    timeout - length of time to scan cars for
#    adapter - bluetooth adapter that you wish to scan with
def scan_cars(adapter, timeout):
  global scan

  # Spawn the subprocess to scan
  command = 'sudo ./drive-sdk/build/dist/bin/vehicle-scan ' + adapter + ' ' + str(timeout) 
  scan = subprocess.Popen(command, shell=True, bufsize=1024, stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
  # Wait for process to spawn
  time.sleep(0.5)

  # Get output from scanning
  (out, err) = scan.communicate(input=None)
  if (scan.poll() == None):
    os.kill(scan.pid, signal.SIGTERM)
    print 'scan process error'
  
  # Get scan output
  return out

# Connect to a car given the name of the car and which bluetooth device to use
#  If no bluetooth device is chosen, the connection will default to hci0
#  Parameters:
#    car - mac address of the car you wish to connect to
#    adapter - bluetooth adapter that you wish to use fo the connection
#  Returns:
#    -1 - if an error has occured
#     0 - if the connection was made correctly
def connect_car(car, adapter):
  #Send the message to the server
  szData = '/connect/'+ car +'/' + adapter
  reply = send_msg(szData)
  
  # Parse the reply message to get return code
  if (parse_reply(reply) > 0):
    return 0
  return -1

# Set the light pattern on a car
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
  # Set parse return code
  parse = 0    

  # Lookup the corresponding index to channel and effect
  ichannels = ["RED", "TAIL", "BLUE", "GREEN", "FRONTL", "FRONTR"]
  ieffects =  ["STEADY", "FADE", "THROB", "FLASH", "RANDOM"]

  # Check car
  wr = '/write/'
  if (car == 'all'):
    wr = '/write_all'
    car = ''

  # Create message
  szData = wr + car + '/set_light_pattern/' 
  for x in range(0, len(ichannels)):
    if (ichannels[x] == channel):
      szData = szData + str(x)
  szData = szData + '/'
  for x in range(0, len(ieffects)):
    if (ieffects[x] == effect):
      szData = szData + str(x)
  szData = szData + '/' + str(start) +'/' + str(end) +'/'+ str(cycles_per_minute)
 
  # Create and send message to server
  reply = send_msg(szData)
  
  # Send return code back to user
  if (parse_reply(reply) < 0):
    parse = -1
  msg = 'RETURN CODE: ' + str(parse)
  log_write(msg)

  return parse

# Set the speed for the motors
#  Parameters:
#    speed - speed for the motors to reach
#    accel - acceleration for the motors to ramp up to speed
#  Returns:
#    -1 - if an error has occured
#     0 - if a message was correctly sent to the car
def set_speed(car, speed, accel):
  global sock
  parse = 0

  # Create message
  wr = '/write/'
  if (car == 'all'):
    wr = '/write_all'
    car = ''
  szData = wr + car + '/set_speed/' + str(speed) + '/' + str(accel)
  
  # Send the sdk_mode_on to the server
  reply = send_msg('/write_all/sdk_mode_on')
  # Get parse reply
  if (parse_reply(reply) < 0):
    parse = -1  

  # Send set speed msg to the server
  reply = send_msg(szData)
  # Get parse reply
  if (parse_reply(reply) < 0):
    parse = -1

  msg = 'RETURN CODE: ' + str(parse) 
  log_write(msg)
  return parse 

# Change the lane of the car
#  Parameters: 
#    car - mac address of the car you wish to connect to (or "all" to send the msg to all cars)
#    speed - speed for the car to move at
#    lane - lane that the car should move to (based on the starting position of the car)
#  Returns:
#    -1 - if an error has occured
#     0 - if a message was correctly sent to the car
def change_lane(car, speed, lane):
  global sock
  # Create the message
  wr = '/write/'
  if (car == 'all'):
    wr = '/write_all'
    car = ''  
  
  # Store result from reply of server
  parse = 0

  # Send offset car message
  szData = wr + car + '/set_offset/0.0'
  reply = send_msg(szData)
  # Ensure the parse is > 0 (no error in return code)
  if (parse_reply(reply) < 0):
    parse = -1

  # Send change lane car message
  szData = wr + car + '/change_lane/' + str(speed) + '/' + str(lane*100.0) + '/'
  reply = send_msg(szData)
  
  # Add the two parse replies together
  if (parse_reply(reply) < 0):
    parse = -1 

  msg = 'RETURN CODE: ' + str(parse)
  log_write(msg)

  return parse

# Disconnect to a car given the name of the car and which bluetooth device to use
#  If no bluetooth device is chosen, the connection will default to hci0
#  Parameters:
#    car - mac address of the car you wish to connect to
#    adapter - bluetooth adapter that you wish to use fo the connection
#  Returns:
#    -1 - if an error has occured
#     0 - if the connection was made correctly
def disconnect_car(car):
  szData = '/write/disconnect/' + car + '/' + adapter
  reply = send_msg(szData)

  if (parse_reply(reply) > 0):
    return 0
  return -1

# End session with the SDK
#  Call this before ending any program.  Automatically disconnects from all cars.
def ANKI_end():
  global server
  global scan
 
  # Send the server a SIGTERM to kill it 
  if (server.poll() == None):
    os.kill(server.pid, signal.SIGTERM)
    os.waitpid(server.pid, 0)

  # Send a SIGTERM to scan process to kill it
  if (scan.poll() == None):
    os.kill(scan.pid, signal.SIGTERM)  
    os.waitpid(scan.pid, 0)
 
  # Exit the program
  sys.exit(0)

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
    msg = 'Send failed on msg' + message
    log_write(msg)
    return ''
 
  log_write('Message sent successfully:')
  log_write(message)

  # Get return reply from the server
  reply = sock.recv(2500)
  log_write(reply)

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
    log_write('Could not find _:_ in message to return error code')
    return -1

  if ((index +1) > len(reply)):
    log_write('Could not find return code in return message')
    return -1
  return reply[index+1:len(reply)]

# Open a socket to the server
def sock_open():
  # Loop for 0.2 seconds and try to open socket
  start = time.clock()
  check = 1
  while (check != 0):
    # Create an AF_INET, STREAM socket (TCP)
    try:
      global sock
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error, msg:
      # Wait for 0.2 seconds for the socket to open, otherwise exit
      if ((time.clock() - start) > 0.2):
        msg = 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
        log_write(msg)
        break
      check = -1
    log_write ('Socket Created')
    check = 0

  # Connect to spawned server process
  HOST = 'localhost'     # connection to server locally
  SERVER_PORT = 2500     # server at port 2500
  sock.connect((HOST, SERVER_PORT)) 

# Close the socket to the server
def sock_close():
  global sock
  sock.close()

# Write to the log file
def log_write(szData):
  filename = 'SDK_py.log'
  fLog = open(filename, "a")
  fLog.write(szData)
  fLog.write("\n")
  fLog.close

# Clear the log file
def log_clear():
  filename = 'SDK_py.log'
  fLog = open(filename, "w+")
  fLog.write("")
  fLog.close
