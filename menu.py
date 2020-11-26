def Menu():
    print("""
                    Please find the MENU below:

                    Press 0 to create parking lot
                    Press 1 to park your car
                    Press 2 to leave the parking lot
                    Press 3 to know car slot by reg_no.
                    Press 4 to know all the slots for cars of particular color
                    press 5 to get the nearest empty slot
                    Press 6 to view the current status of Parking lot
                    Press 7 to view reg_nos for cars of particular color
                    Press 8 to know the no. of empty slots
                    Type MENU/menu to see the Menu at any point of time
                    Type Exit or Quit to end the program

                    """)

def options_to_line():

    Menu()

    option = input("==>")

    if option == "0":
        size = input("Enter the size of parking lot: ")
        name = input("Enter name of parking lot: ")
        return f"create_parking_lot {size} {name}"


    elif option == "1":
        reg_no = input("Enter registration No: ")
        color = input("Enter color: ")
        return f"park {reg_no} {color}"

    elif option == "2":
        slot_no = input("Enter slot number: ")
        return f"leave {slot_no}"
    
    elif option == "3":
        reg_no = input("Enter registration No: ")
        return f"slot_number_for_registration_number {reg_no}"
    
    elif option == "4":
        color = input("Enter color: ")
        return f"slot_numbers_for_cars_with_colour {color}"

    elif option == "5":
        return "nearest_empty_slot"

    elif option == "6":
        return "view_parked_cars"

    elif option == "7":
        color = input("Enter color: ")
        return f"registration_numbers_for_cars_with_colour {color}"

    elif option == "8":
        return "remaining_slots"
    
    elif option.lower() == "menu":
        return "menu"

    elif option.lower() == "exit" or option.lower() == "quit":
        return "exit"




