from pydantic import BaseModel

class Room(BaseModel):
    number: int
    category: str
    price: float
    is_occupied: bool = False 

    def __str__(self) -> str:
        is_occupied_str = "Занят" if self.is_occupied else "Свободен"
        return f"Номер {self.number} | {self.category} | {self.price}$ за ночь | {is_occupied_str}"
