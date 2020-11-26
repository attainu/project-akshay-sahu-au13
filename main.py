import argparse
from Parkinglot import *

if __name__ == "__main__":

	parkinglot = ParkingLot()
	parser = argparse.ArgumentParser(description="For taking input from a file")
	parser.add_argument("-run", action="store", dest="input_file", help="Input File to test the program")
	args = parser.parse_args()

	if args.input_file:
		with open(args.input_file) as f:
			for line in f:
				line = line.rstrip('\n')
				parkinglot.Execute(line)
	else:
		Op = input("Press 1 for menu driven inputs: \nPress any other key for normal user driven inputs: ")
		
		if Op == "1":
			while True:
				line = options_to_line()
				parkinglot.Execute(line)

		else:
			while True:
				line = input("==> ")
				parkinglot.Execute(line)

