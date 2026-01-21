class Booking:
    def __init__(self, name_guest, room, nights) -> None:
        self.name_guest = name_guest
        self.room = room
        self.nights = nights

    def __str__(self) -> str:
        return f"Бронь на имя {self.name_guest}, номер {self.room.number}, на {self.nights} night(s)"