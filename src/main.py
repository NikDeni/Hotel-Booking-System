from models.hotel import Hotel
from models.room import Room
from utils.services import *


hotel = Hotel()

while True:
    show_menu()
    choice = int(input("действие -> "))
    match choice:
        case 1:
            hotel.show_available_rooms()
        case 2:
            book = hotel.book_room(guest_name="Nikolay", nights=2, number=102)
            print(f"Создана {book}")
        case 3:
            hotel.check_out(number=102)
            print("Бронь отменена")
        case 4:
            break
        case _:
            print("Некорректный ввод данных. Попробуйте ещё.")
