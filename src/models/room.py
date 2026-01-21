class Room:
    def __init__(self, number, category, price) -> None:
        self.number = number
        self.category = category
        self.price = price
        self.is_occupied = False

    def __str__(self) -> str:
        is_occupied_str = "Занят" if self.is_occupied else "Свободен"
        return f"Номер {self.number} | {self.category} | {self.price}$ за ночь | {is_occupied_str}"

    