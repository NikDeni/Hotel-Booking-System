import json
from pydantic import TypeAdapter, BaseModel
from pathlib import Path


def find_number(rooms, number):
    return next((room for room in rooms if room.number == number), None)


def show_menu():
    print(
        """Выберете действие: 
          1 - Показать доступные номера
          2 - Создать бронь
          3 - Отменить бронь
          4 - Показать все брони
          5 - Выйти
          """
    )


def save_data(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        data_to_save = [item.model_dump() for item in data]
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)


def load_from_json[T: BaseModel](model_class: type[T], file_path) -> list[T]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    adapter = TypeAdapter(list[model_class])
    return adapter.validate_python(data)


def create_path_to_data(filename):
    return Path(__file__).parent.parent / "data" / filename
