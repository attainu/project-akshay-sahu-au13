# PARKING LOT SYSTEM

## Contents:
 	Description and Features
 	Technology and concepts used
 	Requirements
 	Setup
 	Instructions on how to run the program

## Description and Features:

This project contains basic implementation of Parking lot system using Python. It creates parking lot with given number of slots. The program has following features:

	•	Create a parking lot with given capacity and name
	•	Park a car
	•	Leave parking lot
	•	Check the status of parking lot
	•	Get the nearest empty slot
	•	Get registration numbers of all cars of a particular colour
	•	Get the slot numbers of all cars of a particular colour
	•	Get the slot number of car by registration number
	•	Get total number of empty slots available at the moment

*Inputs to run the program can be provided in three different mode:*
	1.	Using a text file
	2.	User interactive – by typing the commands manually
	3.	User interactive – by choosing options in inbuilt Menu

## Technology and concepts used:
	•	Python 3.8 (Code is made compatible to run in python 2 as well)
	•	OOPS
	•	User defined Modules

## Requirements:
	•	User needs to install Python in their system, use the following link to download and install the latest version of python: https://www.python.org/downloads/

## Setup:  
Follow the below steps to execute or run this project in your system:

		1.	Clone the repository (https://github.com/attainu/project-akshay-sahu-au13.git)

		2.	Install Python in your computer

		3.	Open the folder using shell or VS code/IDE and type: *python main.py* to run it as a user interactive program
			o	Press 1 for menu based interactive interface 
			o	Press 2 or any other key to type the commands manually

		4.	To give inputs from a file, type following command in shell:
			*python main.py –run input_file1.txt*

## Instructions on how to run the program:

 **To run with file input:**

	o	Open the folder containing source code files in shell and type: 
		*python main.py –run input_file1.txt*  (or) 
		*python main.py –run input_file2.txt*

	o	Input files have the all the commands to test the features of Parking lot program, it will generate the output the in the shell window.
 


**To run with User driven input:**

	o	Open the folder containing source code files in shell and type following command: *python main.py*, then press any key except 1 after the prompt.
	o	Now user has to type the commands manually in following format:

		*	To create parking lot of size N and name XYZ:
				*create_parking_lot  N  XYZ*
		*	To park a car:
				*park  reg_no  color*
		*	To leave/vacate the slot:
				*leave  slot_no*
		*	To see the status of parking lot:
				*view_parked_cars*
		*	To get Registration numbers of cars of same color:
				*registration_numbers_for_cars_with_colour White*
		*	To get slot numbers for cars of same color:
				*slot_numbers_for_cars_with_colour White*
		*	To get the nearest empty slot:
				*nearest_empty_slot*
		*	To check the total available empty slots:
				*remaining_slots*
		*	To get slot number for car by registration no.:
				*slot_number_for_registration_number KA-01-HH-7777*
		*	To exit the program:
				*exit*
			

**To run with Menu driven input:**

		o	Open the folder containing source code files in shell and type: *python main.py*, then press 1 after the prompt to see the menu.
	

		o	Read the options and press the keys accordingly, for eg.
		Press 0 to create a parking lot, the program will ask you to enter the capacity as well as name of the parking lot

		o	Similarly, you can check the menu and press the respective key/number to perform the operation mentioned in the menu.
