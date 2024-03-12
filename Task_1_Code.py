def bookingFunction():
    # Initial seating arrangement
    seats = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    bookSeat(seats)

def printSeatingPlan(seats):
    print("  A B C D E F G H I J")
    rowNumber = 1
    for row in seats:
        print(f"{rowNumber} ", end='')
        rowNumber += 1
        for seat in row:
            if seat == 0:
                print('-', end=' ')
            else:
                print('X', end=' ')
        print()  # Move to the next line after printing each row

def bookSeat(seats):
    print("Current seating plan:")
    printSeatingPlan(seats)
    howManySeats= int(input("how many seats do you want to book? "))
    children= input("How many children? ")
    adults= input("How many adults? ")
    students= input("How many students? ")
    concessionHolders= input("How mant concession holders? ")
    
    # Correcting the error by ensuring proper conversion
    while howManySeats > 0:
        howManySeats = howManySeats - 1
        selection = input("Choose a seat (e.g., 2D): ")
        try:
            row = int(selection[0]) - 1  # Converts the first character to row index
            col = ord(selection[1].upper()) - ord('A')  # Converts the letter to column index
            if 0 <= row < len(seats) and 0 <= col < len(seats[0]):  # Check if the selection is within the range
                if seats[row][col] == 0:
                    seats[row][col] = 1
                    print("Seat booked successfully!\n")
                else:
                    print("Sorry, that seat is already taken.\n")
            else:
                print("Invalid seat selection.\n")
        except (IndexError, ValueError):
            print("Invalid input format. Please use the format <RowNumber><ColumnLetter> (e.g., 2D).\n")
        print("Updated seating plan:")
        printSeatingPlan(seats)




def cancelFunction():
    pass

def endFunction():
    exit()

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