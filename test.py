def Seating():
    seats = [
    [1, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    ]
    #Return array to the rest of the program
    return(seats)

def PrintSeating(seats):
    #Print letters
    print("  A B C D E F G H I J")
    #Creates variable ans sets it to 1
    rowNumber = 1
    #For row in seats prints the row number and row. If value in array = 0 it prints - and if value = 1 it prints X
    for row in seats:
        print(f"{rowNumber} ", end='')
        rowNumber += 1
        for seat in row:
            if seat == 0:
                print('-', end=' ')
            else:
                print('X', end=' ')
        print()

class Booking:
    customerName = ""
    ticketID = 0
    whatSeatsBooked = ""
    totalSeatsBooked = 0
    typePerson = ""
    totalCost = 0

    def getCustomerName(customerName):
        