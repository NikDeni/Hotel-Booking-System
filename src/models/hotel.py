from models.room import Room
from models.booking import Booking
from utils.services import *

class Hotel:
    def __init__(self) -> None:
        self.rooms = load_from_json(model_class=Room, file_path='rooms.json')
        self.bookings = []

    def show_available_rooms(self):
        available_rooms = [room for room in self.rooms if not room.is_occupied]
        
        if not available_rooms:
            print("Все номера заняты")
        else:
            for room in available_rooms:
                print(room)


    def book_room(self, number, guest_name, nights):
        room = find_number(number=number, rooms=self.rooms)
        
        if not room:
            raise ValueError(f"Номер {number} не найден")
        
        if room.is_occupied:
            raise ValueError(f"Номер {number} уже занят")
        
        book = Booking(name_guest=guest_name, nights=nights, room=room)
        self.bookings.append(book)
        room.is_occupied = True

        return book

    def show_all_bookings(self):
        if not self.bookings:
            print("Броней нет")
        else:
            for booking in self.bookings:
                print(booking)

    def check_out(self, number):
        room = find_number(number=number, rooms=self.rooms)
        
        if not room:
            raise ValueError(f"Номер {number} не найден")
        
        booking = next((b for b in self.bookings if b.room == room), None)
        
        if not booking:
            raise ValueError(f"Нет брони для номера {number}")
        
        self.bookings.remove(booking)
        room.is_occupied = False

    def __str__(self) -> str:
        return '\n'.join(str(room) for room in self.rooms)