def bookingFunction():
    pass

def cancelFunction():
    pass

def endFunction():
    pass

def programFunction():
    print("\nTo book a ticket type 'Booking' \nTo cancel a booking type 'Cancel' \nTo end program type 'End'\n")
    userInput = input("What would you like to do? ")
    userInput = userInput.lower()

    match userInput:
        case "booking":
            bookingFunction()
        
        case "cancel":
            cancelFunction()

        case "end":
            endFunction()
        
        case _:
            print("\nIncorect entry please check your spelling and try again\n")
            programFunction()

programFunction()