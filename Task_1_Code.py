# Importing extensions for the program to work
import os
import glob
import random

#Save directory path to a variable
directory= os.getcwd()

#Defines CLASS Booking
class Booking:

    #Defines METHOD Seating
    def seating(self,seats):
        #Creates the array that contains the seating arrangement
        seats = [
        [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
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

    #Defines METHOD printSeating
    def printSeating(self, seats):
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

    #Defines METHOD bookSeat
    def bookSeat(self):
        #Gets the seats and prints them from the METHOD seating and printSeating
        print("\n\n\nCurrent seating plan:")
        seats = []
        seats = b.seating(seats)
        b.printSeating(seats)
        #Exception handling. Try the user input and if incorect value is entered runs the except and prints the error statement and runs the METHOD bookSeat
        try:
            howManySeats= int(input("how many seats do you want to book? "))
        except (IndexError, ValueError):
            print("Invalid input format. Please use integers.")
            b.bookSeat()
        
        #Creates the personPrices dictionary
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

        #Creates an empty array
        results = []

        #Makes sure that the selection is more than 0
        if howManySeats > 0:
            #Calls the METHOD processingBooking
            b.processingBooking(results,personPrices,howManySeats,seats)
        #If selection was less than 0
        else:
            #Print error message and calls the METHOD bookSeat
            print("you have not entered an integer above 0. Please try again")
            b.bookSeat()

    #Defines METHOD processingBooking
    def processingBooking(self, results,personPrices,howManySeats,seats):

        #Converts variable into an integer
        howManySeats = int(howManySeats)
        #Saves how many seats user wanted to book in a different variable for latter use
        totalSeats = howManySeats
        #Creates an empty array
        seatsBooked = []
        
        #While howManySeats is greater than 0 it will keep iterating through the loop
        while howManySeats > 0:
            #Gets user input for what seat they want to book
            selection = input("Choose a seat (e.g., 2D): ")
            #
            typePersonInput = input("If seat is for adult type: A\nIf seat is for a child type: C\nIf seat is for a student type: S\nIf seat is for a concession holder type: H\nWho is seat for? ")
            print(selection[0])
            if not selection[0].isdigit():

                print("Invalid input format. Please use the format <RowNumber><ColumnLetter> (e.g., 2D).\n")
                b.processingBooking(results,personPrices,howManySeats,seats)
    
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
                                    seatsBooked.append(selection)
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
                b.printSeating(seats)
        
        b.receiptFunction(results, totalSeats, seatsBooked)

    def receiptFunction(self, results, totalSeats, seatsBooked):
        seatsBooked=str(seatsBooked).replace("'","").replace("[","").replace("]","")
        randomNumber = ''.join(random.choices('0123456789', k=8))
        txtFiles = glob.glob(os.path.join(directory, "*.txt"))
        fileNames = [os.path.basename(txtFile) for txtFile in txtFiles]
        for fileName in fileNames:
            fileName = fileName.replace(".","_")
            fileName = fileName.split("_")
            receiptID = int(fileName[1])
            if receiptID == int(randomNumber):
                randomNumber = ''.join(random.choices('0123456789', k=8))
            else:
                file = open(f"Reciept_{randomNumber}.txt", "a")
                file.write(f"======================================\nReciept ID: {randomNumber}\nTotal seats Booked: {totalSeats}\nSeats Booked: {seatsBooked}\n\nType Of Seat - Price - Runing Total\n")
                break

        price = 0
        for result in results:
            result = str(results).split()
            resultTypePerson = result[1]
            resultTypePerson = resultTypePerson.replace("h","CONCESSION HOLDER").replace("a","ADULT").replace("c","CHILD").replace("s","STUDENT").replace(",","").replace("'","")
            resultPrice = result[3]
            resultPrice = str(resultPrice).replace("}","")
            resultPrice = float(resultPrice)
            price = price + resultPrice
            file.write(f"{resultTypePerson} - {resultPrice} - {price}\n")

        file.write(f"\nTotal Price: {price}\n======================================\n\n\n\n")
        file.close()
        print(f"\nyou have booked {totalSeats}. This will cost ${price}\nA reciept will be sent to you soon\nYour reciept ID is: {randomNumber}")

class Cancel:
    
    def userInput(self):
        try:
            userInput = int(input("Please enter your ticket ID: "))
        except (IndexError, ValueError):
            print("Invalid input format. Please use integers.")
            c.userInput()
        c.findTicket(userInput)

    def findTicket(self, userInput):
        txtFiles = glob.glob(os.path.join(directory, "*.txt"))
        fileNames = [os.path.basename(txtFile) for txtFile in txtFiles]
        for fileName in fileNames:
            originalFileName = fileName
            fileName = fileName.replace(".","_")
            fileName = fileName.split("_")
            print(fileName[1])
            recieptID = int(fileName[1])
            if recieptID == userInput:
                c.getSeats(originalFileName)
                break
            else:
                continue
        print(f"There is no ticket with ID of '{userInput}'")
        programFunction()

    def getSeats(self,originalFileName):
        file = open(originalFileName,"r")
        lines = file.readlines()
        file.close()
        fourthLine = lines[3]
        fourthLine = fourthLine.split(":")
        ticketSeats = fourthLine[1].replace(" ","")
        ticketSeats = ticketSeats.replace("'","").replace("\n'","")
        c.vacateSeats(ticketSeats, originalFileName)
    
    def vacateSeats(self, ticketSeats, originalFileName):
        seats = []
        seats = b.seating(seats)
        ticketSeats = str(ticketSeats).split(",")
        for ticketseat in ticketSeats:
            row = int(ticketseat[0]) - 1  # Converts the first character to row index
            col = ord(ticketseat[1].upper()) - ord('A')  # Converts the letter to column index
            if 0 <= row < len(seats) and 0 <= col < len(seats[0]):  # Check if the selection is within the range
                if seats[row][col] == 1:
                    seats[row][col] = 0
                    break
                else:
                    print("Seat is already empty. Continuing onto next seat\n")
                    continue
            else:
                print("Sorry, we encounted an error. Continuing to next seat.\n")
                continue
        os.remove(originalFileName)


        


def endFunction():
    exit()

def programFunction():
    print("\n\n\n\n\nTo book a ticket type 'Booking' \nTo cancel a booking type 'Cancel' \nTo end program type 'End'\n")
    userInput = input("What would you like to do? ")
    userInput = userInput.lower()

    match userInput:
        case "booking":
            b.bookSeat()
        
        case "cancel":
            c.userInput()

        case "end":
            endFunction()
        
        case _:
            print("\nIncorrect entry please check your spelling and try again\n")
            programFunction()

b = Booking()
c = Cancel()
programFunction()