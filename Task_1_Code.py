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
            #Gets user input
            typePersonInput = input("If seat is for adult type: A\nIf seat is for a child type: C\nIf seat is for a student type: S\nIf seat is for a concession holder type: H\nWho is seat for? ")
            #Print selection
            print(selection[0])

            #Checks if selection[0] is not a digit
            if not selection[0].isdigit():
                #Print error message and calls METHOD processingBooking
                print("Invalid input format. Please use the format <RowNumber><ColumnLetter> (e.g., 2D).\n")
                b.processingBooking(results,personPrices,howManySeats,seats)
            #If is a digit        
            else: 
                #Tries the folowing code
                try:
                    #Seperates the row and column index from the selection
                    row = int(selection[0]) - 1
                    col = ord(selection[1].upper()) - ord('A')

                    #Checks if selection is within the range of the array
                    if 0 <= row < len(seats) and 0 <= col < len(seats[0]):
                        if seats[row][col] == 0:
                            #Check if typePersonInput is in person prices
                            for staff_id, record in personPrices.items():
                                if typePersonInput.lower() in record["name"].split()[-1].lower():
                                    #Change the item in array from 0 to 1
                                    seats[row][col] = 1
                                    #Update the result array
                                    results.append(record)
                                    #Subtracts 1 from the variable untill the while loop stops
                                    howManySeats -= 1
                                    #Prints a message to say booking was succesfull and updates the array
                                    print("Seat booked successfully!\n")
                                    seatsBooked.append(selection)
                                    #Stops the loop
                                    break
                                #If item is not in record
                                else:
                                    #Print error message and continue on with program
                                    print("Invalid type of person input. Please try again")
                                    continue 
                        #If does not equal 0  prints error message
                        else:
                            print("Sorry, that seat is already taken.\n")
                    #If seat is out of array range print error message
                    else:
                        print("Invalid seat selection.\n")
                #If code breaks in try prints error message
                except (IndexError, ValueError):
                    print("Invalid input format. Please use the format <RowNumber><ColumnLetter> (e.g., 2D).\n")

                #Print the seating plan
                print("Updated seating plan:")
                b.printSeating(seats)
        
        #Calls METHOD receiptFunction
        b.receiptFunction(results, totalSeats, seatsBooked)

    #Defines METHOD recieptFunction
    def receiptFunction(self, results, totalSeats, seatsBooked):
        #Turns variable into string and removes unwated characters
        seatsBooked=str(seatsBooked).replace("'","").replace("[","").replace("]","")
        #Gets a random number
        randomNumber = ''.join(random.choices('0123456789', k=8))
        #Searches for all txt files and saves there names to a variable
        txtFiles = glob.glob(os.path.join(directory, "*.txt"))
        fileNames = [os.path.basename(txtFile) for txtFile in txtFiles]
        #For fileName in fileNames it changes unwated characters and splits the name into parts
        for fileName in fileNames:
            fileName = fileName.replace(".","_")
            fileName = fileName.split("_")
            #Gets the part of file name that has the reciept ID
            receiptID = int(fileName[1])
            #Checks if any of the existing receipts have the same number as the randomly generated one
            if receiptID == int(randomNumber):
                b.receiptFunction()
            ###########################################################################################################################################
            else:
                continue
        
        #Sets variable to equal 0
        price = 0
        
        ###########################################################################################################################################
        file = open(f"Reciept_{randomNumber}.txt", "w")
        file.write(f"======================================\nReciept ID: {randomNumber}\nTotal seats Booked: {totalSeats}\nSeats Booked: {seatsBooked}\n\nType Of Seat - Price - Runing Total\n")

        #For result in results it turns to a string and splits it
        for result in results:
            result = str(results).split()
            #Gets the type of person from the string and replaces the placeholder letter with the full name
            resultTypePerson = result[1]
            resultTypePerson = resultTypePerson.replace("h","CONCESSION HOLDER").replace("a","ADULT").replace("c","CHILD").replace("s","STUDENT").replace(",","").replace("'","")
            #Gets the price related to the type of person and removes unwated characters before tunring into a float
            resultPrice = result[3]
            resultPrice = str(resultPrice).replace("}","").replace(",","").replace("'","").replace("]","")
            resultPrice = float(resultPrice)
            #Adds the price for the person to the total price
            price = price + resultPrice
            #Adds the type of person, price for there ticket and running price to the ticket/reciept
            file.write(f"{resultTypePerson} - {resultPrice} - {price}\n")

        #Writes total price to the ticket and closes the file
        file.write(f"\nTotal Price: {price}\n======================================\n\n\n\n")
        file.close()
        #Prints how many seats the customer booked, the total cost and the receipt ID
        print(f"\nyou have booked {totalSeats}. This will cost ${price}\nA reciept will be sent to you soon\nYour reciept ID is: {randomNumber}")

        programFunction()

#Defines CLASS Cancel
class Cancel:
    
    #Defines METHOD userInput
    def userInput(self):
        #Tries the user input
        try:
            userInput = int(input("Please enter your ticket ID: "))
        #If encounters an error print error message and call METHOD userInput
        except (IndexError, ValueError):
            print("Invalid input format. Please use integers.")
            c.userInput()
        #Calls METHOD findTicket
        c.findTicket(userInput)

    #Defines METHOD findTicket
    def findTicket(self, userInput):
        #Search for all text files in folder and saves the name into a variable
        txtFiles = glob.glob(os.path.join(directory, "*.txt"))
        fileNames = [os.path.basename(txtFile) for txtFile in txtFiles]
        #For fileName in fileNames it changes unwated characters and splits the name into parts and saves original name to a variable
        for fileName in fileNames:
            originalFileName = fileName
            fileName = fileName.replace(".","_")
            fileName = fileName.split("_")
            #Gets the part of file name that has the reciept ID
            recieptID = int(fileName[1])
            #Checks if receipt ID equals users input
            if recieptID == userInput:
                #Calls METHOD getsSeats and stops the loop
                c.getSeats(originalFileName)
                break
            #If doesnt equal userinput continue the program
            else:
                continue
        #Print error message and calls FUNCTION programFunction
        print(f"There is no ticket with ID of '{userInput}'")
        programFunction()

    #Defines METHOD getSeats
    def getSeats(self,originalFileName):
        #Opens file in read mode and reades the lines
        file = open(originalFileName,"r")
        lines = file.readlines()
        file.close()
        #Saves the fourth line of the txt file
        fourthLine = lines[3]
        fourthLine = fourthLine.split(":")
        #Seperates the seats from the rest of information on that line
        ticketSeats = fourthLine[1].replace(" ","")
        ticketSeats = ticketSeats.replace("'","").replace("\n'","")
        #Calls METHOD vacateSeats
        c.vacateSeats(ticketSeats, originalFileName)
    
    #Defines METHOD vacateSeats
    def vacateSeats(self, ticketSeats, originalFileName):
        #Gets seats array from METHOD seating in class booking
        seats = []
        seats = b.seating(seats)
        #Tunrs into a string and splits them into individual seats
        ticketSeats = str(ticketSeats).split(",")
        #For ticketseat in ticketSeats
        for ticketseat in ticketSeats:
            #Seperates the row and column index from the selection
            row = int(ticketseat[0]) - 1 
            col = ord(ticketseat[1].upper()) - ord('A')
            #Checks if selection is within the range of the array
            if 0 <= row < len(seats) and 0 <= col < len(seats[0]):
                #Checks if item in array is equal to 1
                if seats[row][col] == 1:
                    #Change the item in array from 1 to 0
                    seats[row][col] = 0
                #If seat is not equal to 1 print error message and continue the program
                else:
                    print("Seat is already empty. Continuing onto next seat\n")
                    continue
            #If not in array print error message and continue with program
            else:
                print("Sorry, we encounted an error. Continuing to next seat.\n")
                continue
        #Remove the text file from folder
        os.remove(originalFileName)

        programFunction()


        


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