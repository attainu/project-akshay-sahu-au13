from menu import *
import sys
from Vehicle import *


if sys.version_info[0] == 2:
	input = raw_input


class ParkingLot:

    def __init__(self):
        self.size = 0
        self.slot_no = 0
        self.total_parked_slots = 0


    def create_Parking_Lot(self, size):
        self.slots = [0] * size
        self.size = size
        return self.size


    def get_nearest_slot(self):
        for slot in range(self.size):
            if self.slots[slot] == 0:
                return slot


    def park_car(self,registration_no, color):
        if self.total_parked_slots < self.size: 
            slot_no = self.get_nearest_slot()
            self.slots[slot_no] = Car(registration_no, color)
            self.slot_no = self.slot_no+1
            self.total_parked_slots = self.total_parked_slots + 1
            return slot_no + 1
        else:
            return -1


    def no_of_empty_slots(self):
        return (self.size - self.total_parked_slots)


    def leave(self,slot_no):

        if self.total_parked_slots > 0 and self.slots[slot_no-1] != 0:
            self.slots[slot_no - 1] = 0
            self.total_parked_slots = self.total_parked_slots - 1
            return "Left"
        else:
            return "Already Empty"


    def view_parked_cars(self):
        print("Slot No.\tRegistration No.\tColour")
        for i in range(self.size):
            if self.slots[i] != 0:
                print(f"{i+1} \t\t {self.slots[i].reg_no} \t\t {self.slots[i].color}")
            else:
                print(f"{i+1} \t\t ((EMPTY))\t\t((EMPTY))")


    def get_registration_no_by_color(self,color):

        registration_nos = []
        for i in self.slots:

            if i == 0:
                continue

            if i.color.lower() == color.lower():
                registration_nos.append(i.reg_no)

        return registration_nos


    def slot_numbers_by_reg_no(self,registration_no):
        
        for i in range(self.size):
            if self.slots[i].reg_no == registration_no:
                return i+1
            else:
                continue
        return -1
            

    def slot_numbers_by_color(self,color):
        
        slot_numbers = []

        for i in range(self.size):

            if self.slots[i] == 0:
                continue
            if self.slots[i].color.lower() == color.lower():
                slot_numbers.append(str(i+1))
        return slot_numbers


    def Execute(self,line):

        if line.startswith('create_parking_lot'):
            n = int(line.split(" ")[1])
            name = " ".join(line.split(" ")[2:])
            res = self.create_Parking_Lot(n)
            print(f"Parking lot {name} created with capacity of {n} vehicles")

        elif line.startswith("remaining_slots"):
            print(f"There are {self.no_of_empty_slots()} empty slots available")

        elif line.startswith("nearest_empty_slot"):
            print(f"Nearest available slot is {self.get_nearest_slot()+1}")

        elif line.startswith("park"):
            registration_no = line.split(" ")[1]
            color = line.split(" ")[2]
            slot = self.park_car(registration_no,color)
            if slot == -1:
                print("Parking lot is full, can't accomodate more vehicles... SORRY!")
            else:
                print(f"Please park your car in allocated slot : {slot}")

        elif line.startswith("view_parked_cars"):
            self.view_parked_cars()

        elif line.startswith("registration_numbers_for_cars_with_colour"):
            color = line.split(" ")[1]
            registration_nos = self.get_registration_no_by_color(color)
            print(', '.join(registration_nos))

        elif line.startswith("slot_numbers_for_cars_with_colour"):
            color = line.split(" ")[1]
            slot_numbers = self.slot_numbers_by_color(color)
            print(', '.join(slot_numbers))

        elif line.startswith("leave"):
            leave_slot = int(line.split(" ")[1])
            status = self.leave(leave_slot)

            if status == "Left":
                print(f"Vacated slot number {leave_slot}")
            else:
                print(f"The slot number {leave_slot} is already Vacant")

        elif line.startswith("slot_number_for_registration_number"):
            registration_no = line.split(" ")[1]
            slot_no = self.slot_numbers_by_reg_no(registration_no)
            if slot_no == -1:
                print("No such car is Parked here")
            else:
                print(f"The car with registration no. {registration_no} is parked in slot {slot_no}")
        
        elif line.startswith("exit"):
            print("Thank you, for using our Parking station, Visit Again!!!")
            exit(0)

        elif line.startswith("menu"):
            Menu()