from models.room import Room
from models.booking import Booking
from utils.services import *

class Hotel:
    def __init__(self, rooms: list[Room]) -> None:
        self.rooms = rooms
        self.bookings = []

    def show_available_rooms(self):
        is_occupied_all = True
        for room in self.rooms:
            if not room.is_occupied:
                is_occupied_all = False
                print(room)
        
        if is_occupied_all:
            print("Все номера заняты")

    def book_room(self, number, guest_name, nights):
        room = find_number(number=number, rooms=self.rooms)
        book = Booking(name_guest=guest_name, nights=nights, room=room)
        self.bookings.append(book)
        if room:
            room.is_occupied = True

        return book

    def show_all_bookings(self):
        for booking in self.bookings:
            print(booking)
        
        if not self.bookings:
            print("Броней нет")

    def check_out(self, number):
        room = find_number(number=number, rooms=self.rooms)
        booking = next((booking for booking in self.bookings if booking.room == room), None)
        self.bookings.remove(booking)
        if room:
            room.is_occupied = False

    def __str__(self) -> str:
        result_str = ''
        for room in self.rooms:
            result_str += str(room)
            result_str += '\n'
        
        return result_str