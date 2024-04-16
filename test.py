import os
import glob
import random

class SeatingArrangement:
    def __init__(self):
        self._seats = [
            [1, 0, 0, 0, 1, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        ]

    def get_seats(self):
        return self._seats

    def print_seating(self):
        print("  A B C D E F G H I J")
        row_number = 1
        for row in self._seats:
            print(f"{row_number} ", end='')
            row_number += 1
            for seat in row:
                print('X' if seat else '-', end=' ')
            print()

    def book_seat(self, row, col):
        if 0 <= row < len(self._seats) and 0 <= col < len(self._seats[0]):
            if self._seats[row][col] == 0:
                self._seats[row][col] = 1
                return True
            else:
                print("Sorry, that seat is already taken.")
        else:
            print("Invalid seat selection.")
        return False

    def cancel_seat(self, row, col):
        if 0 <= row < len(self._seats) and 0 <= col < len(self._seats[0]):
            if self._seats[row][col] == 1:
                self._seats[row][col] = 0
                return True
            else:
                print("Seat is already empty.")
        else:
            print("Invalid seat selection.")
        return False

class BookingManager:
    def __init__(self, seating_arrangement):
        self._seating_arrangement = seating_arrangement
        self._person_prices = {
            "adult": {"name": "adult", "price": 30.00},
            "child": {"name": "child", "price": 10.00},
            "student": {"name": "student", "price": 5.00},
            "concession_holder": {"name": "concession holder", "price": 15.00},
        }

    def book_seats(self):
        seats_booked = []
        results = []
        total_seats = self._get_number_of_seats()
        seats = self._seating_arrangement.get_seats()

        while total_seats > 0:
            selection = self._get_seat_selection()
            person_type = self._get_person_type()

            if self._is_valid_seat_selection(selection):
                row, col = self._parse_seat_selection(selection)

                if self._seating_arrangement.book_seat(row, col):
                    seats_booked.append(selection)
                    person_record = self._get_person_record(person_type)
                    if person_record:
                        results.append(person_record)
                        total_seats -= 1

        receipt_id = self._generate_receipt_id()
        self._generate_receipt(receipt_id, total_seats, seats_booked, results)
        print(f"You have booked {len(seats_booked)} seats. Your receipt ID is: {receipt_id}")

    def _get_number_of_seats(self):
        while True:
            try:
                num_seats = int(input("How many seats do you want to book? "))
                if num_seats > 0:
                    return num_seats
                else:
                    print("Number of seats must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def _get_seat_selection(self):
        while True:
            selection = input("Choose a seat (e.g., 2D): ")
            if self._is_valid_seat_selection(selection):
                return selection
            else:
                print("Invalid seat selection. Please try again.")

    def _is_valid_seat_selection(self, selection):
        if len(selection) != 2:
            return False
        if not selection[0].isdigit() or not selection[1].isalpha():
            return False
        return True

    def _parse_seat_selection(self, selection):
        row = int(selection[0]) - 1
        col = ord(selection[1].upper()) - ord('A')
        return row, col

    def _get_person_type(self):
        while True:
            person_type = input(
                "Who is the seat for?\n"
                "A: Adult\n"
                "C: Child\n"
                "S: Student\n"
                "H: Concession Holder\n"
                "Enter your choice: "
            ).lower()
            if person_type in self._person_prices:
                return person_type
            else:
                print("Invalid person type. Please try again.")

    def _get_person_record(self, person_type):
        return self._person_prices.get(person_type)

    def _generate_receipt_id(self):
        directory = os.getcwd()
        existing_files = glob.glob(os.path.join(directory, "Receipt_*.txt"))
        existing_ids = [int(os.path.basename(f).split("_")[1].split(".")[0]) for f in existing_files]

        while True:
            receipt_id = ''.join(random.choices('0123456789', k=8))
            if int(receipt_id) not in existing_ids:
                return receipt_id

    def _generate_receipt(self, receipt_id, total_seats, seats_booked, results):
        directory = os.getcwd()
        filename = f"Receipt_{receipt_id}.txt"
        filepath = os.path.join(directory, filename)

        with open(filepath, "w") as file:
            file.write("======================================\n")
            file.write(f"Receipt ID: {receipt_id}\n")
            file.write(f"Total seats Booked: {total_seats}\n")
            file.write(f"Seats Booked: {', '.join(seats_booked)}\n\n")
            file.write("Type of Seat - Price - Running Total\n")

            total_price = 0
            for result in results:
                price = result["price"]
                total_price += price
                file.write(f"{result['name'].upper()} - {price:.2f} - {total_price:.2f}\n")

            file.write(f"\nTotal Price: {total_price:.2f}\n")
            file.write("======================================\n")

class CancelManager(BookingManager):
    def __init__(self, seating_arrangement):
        super().__init__(seating_arrangement)

    def cancel_booking(self):
        receipt_id = self._get_receipt_id()
        if receipt_id:
            seats_to_cancel = self._get_seats_from_receipt(receipt_id)
            if seats_to_cancel:
                self._cancel_seats(seats_to_cancel)
                self._delete_receipt(receipt_id)
                print("Booking canceled successfully.")
            else:
                print("No seats found for the provided receipt ID.")
        else:
            print("Invalid receipt ID.")

    def _get_receipt_id(self):
        while True:
            try:
                receipt_id = int(input("Please enter your receipt ID: "))
                return receipt_id
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def _get_seats_from_receipt(self, receipt_id):
        directory = os.getcwd()
        filename = f"Receipt_{receipt_id}.txt"
        filepath = os.path.join(directory, filename)

        try:
            with open(filepath, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith("Seats Booked:"):
                        seats_booked = line.split(":")[1].strip()
                        return [seat.strip() for seat in seats_booked.split(",")]
        except FileNotFoundError:
            return None

    def _cancel_seats(self, seats_to_cancel):
        for seat in seats_to_cancel:
            row, col = self._parse_seat_selection(seat)
            self._seating_arrangement.cancel_seat(row, col)

    def _delete_receipt(self, receipt_id):
        directory = os.getcwd()
        filename = f"Receipt_{receipt_id}.txt"
        filepath = os.path.join(directory, filename)
        os.remove(filepath)

class UserInterface:
    def __init__(self):
        self._seating_arrangement = SeatingArrangement()
        self._booking_manager = BookingManager(self._seating_arrangement)
        self._cancel_manager = CancelManager(self._seating_arrangement)

    def run(self):
        while True:
            self._print_menu()
            choice = input("Enter your choice: ").lower()

            if choice == "b":
                self._booking_manager.book_seats()
            elif choice == "c":
                self._cancel_manager.cancel_booking()
            elif choice == "e":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")

    def _print_menu(self):
        print("\n==== Ticket Booking System ====")
        print("B: Book Seats")
        print("C: Cancel Booking")
        print("E: Exit")

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()