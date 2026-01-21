from pydantic import BaseModel
from models.room import Room


class Booking(BaseModel):
    name_guest: str
    room: Room
    nights: int

    def __str__(self) -> str:
        return f"Бронь на имя {self.name_guest}, номер {self.room.number}, на {self.nights} night(s)"
