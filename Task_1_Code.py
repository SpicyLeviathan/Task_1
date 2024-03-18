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
    try:
        howManySeats= int(input("how many seats do you want to book? "))
    except (IndexError, ValueError):
        print("Invalid input format. Please use integers.")
        bookingFunction()
    
    personPrices = {
        "adult": { 
            "name": 'a',
            "price": 30.00
        },
        "child": { 
            "name": 'c',
            "price": 10.00
        },
        "student": { 
            "name": 's',
            "price": 5.00
        },
        "concession_holder": { 
            "name": 'h',
            "price": 15.00
        }
    }

    results = []

    if howManySeats > 0:
        makingBooking(results,personPrices,howManySeats,seats)
    else:
        print("you have not entered an integer above 0. Please try again")
        bookingFunction()



def makingBooking(results,personPrices,howManySeats,seats):

    howManySeats = int(howManySeats)
    totalSeats = howManySeats
    # Correcting the error by ensuring proper conversion
    while howManySeats > 0:
        selection = input("Choose a seat (e.g., 2D): ")
        typePersonInput = input("If seat is for adult type: A\nIf seat is for a child type: C\nIf seat is for a student type: S\nIf seat is for a concession holder type: H\nWho is seat for? ")
        print(selection[0])
        if not selection[0].isdigit():

            print("Invalid input format. Please use the format <RowNumber><ColumnLetter> (e.g., 2D).\n")
            makingBooking(results,personPrices,howManySeats,seats)
   
        else: 
            try:
                row = int(selection[0]) - 1  # Converts the first character to row index
                col = ord(selection[1].upper()) - ord('A')  # Converts the letter to column index

                if 0 <= row < len(seats) and 0 <= col < len(seats[0]):  # Check if the selection is within the range
                    if seats[row][col] == 0:
                        # Check if typePersonInput is in person prices
                        for staff_id, record in personPrices.items():
                            if typePersonInput.lower() in record["name"].split()[-1].lower():
                                seats[row][col] = 1
                                results.append(record)
                                howManySeats -= 1
                                print("Seat booked successfully!\n")
                                break
                        else:
                            print("Invalid type of person input. Please try again")
                            continue  # Skip to the next iteration if typePersonInput is invalid
                    else:
                        print("Sorry, that seat is already taken.\n")
                else:
                    print("Invalid seat selection.\n")
            except (IndexError, ValueError):
                print("Invalid input format. Please use the format <RowNumber><ColumnLetter> (e.g., 2D).\n")

            print("Updated seating plan:")
            printSeatingPlan(seats)
    
    receiptFunction(results, totalSeats)

def receiptFunction(results,totalSeats):
    price = 0
    for result in results:
        result = str(result).split()
        print(result)
        resultTypePerson = result[1]
        print(resultTypePerson)
        resultTypePerson = resultTypePerson.replace("h","Concession Holder").replace("a","Adult").replace("c","Child").replace("s","Student")
        print(resultTypePerson)

        resultPrice = result[3]
        resultPrice = str(resultPrice).replace("}","")
        resultPrice = float(resultPrice)
        print(resultPrice)

        price = price + resultPrice

    print(f"you have booked {totalSeats}. This will cost ${price}\nA reciept will be sent to you soon.")


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