#!/usr/bin/python

import SDK
import sys, getopt, subprocess

position_info = []
change_speed = 20

#writing to last position file
def update_pos(num_cars, argv):

	for x in range(0, num_cars):
		#open(argv[x+1] + "pos")
		global position_info
		fLog = open('lastPos', 'w')
		position = open(get_car_id(argv[x]).readlines())
		position_length = len(position)
		position_information = position[position.length - 1].split("(")
		position_information = position_information[2].split(", ")
		for y in range(0, 3):
			fLog.write(str(x) + position_information + " ")
			position_info.append(str(x) + position_information)
		fLog.write("\n");
		fLog.close()
		position.close()

def main(argv):
	global position_info
	global change_speed
	commands = ['shoot', 'speed_up','move_left', 'move_right', 'slow_down']
	energy = []
	car_names = []
	shoot_commands = []
	place = []
	turns = 5;
	count = 0;
	num_cars = len(argv) - 1
	starting_offset = 130
	SDK.ANKI_start()

	for x in range(0, num_cars):
		SDK.connect_car("mac address here")
		car_names.append(argv[x+1])
		energy.append(10)
		SDK.send_start_position(argv[x], starting_offset)
		starting_offset -= (starting_offset / num_cars)
		place.append("")
	#update_pos(num_cars, argv)
	#gameplay
	for x in range(0, turns):
		for y in range(0, num_cars):
			start = time.clock()
			subprocess.call(("./" + car_names[y]), shell = True)
			moves = fopen(car_names[y] + "move").readlines()
			print moves[0] + " " + commands[0]
			if energy[y] != 0
				if moves[0] == commands[0]
					shoot_commands.append(car_names[y])
					energy[y] -= 1
				elif moves[0] == commands[1]
					SDK.set_speed(car_names[y], position_info[4 * y - 1] + change_speed, 10)
					energy[y] -= 1
				elif moves[0] == commands[2]
					SDK.change_lane(car_names[y], position_info[4 * y - 1], -2)
					energy[y] -= 0
				elif moves[0] == commands[3]
					SDK.change_lane(car_names[y], position_info[4 * y - 1], 2)
					energy[y] -= 0
				elif moves[0] == commands[4]
					SDK.set_speed(car_names[y], position_info[4 * y - 1] - change_speed, 10)
					energy[y] += 1
				if energy[y] == 0
					place.append(car_names[y]);
		for z in shoot_commands
			set_lights(shoot_commands[z], "FRONTL", "FLASH", 1, 4, 1)
			set_lights(shoot_commands[z], "FRONTR", "FLASH", 1, 4, 1)
		if((time.clock() - start) > 15)
			#turn off lights
		for y in range(0, num_cars):

		del position_info[:]
		del shoot_commands[:]


	SDK.ANKI_end()
	print ++count + ". " + reversed(place)

main(sys.argv)

