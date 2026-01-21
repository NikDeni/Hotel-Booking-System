def find_number(rooms, number):
    return next((room for room in rooms if room.number == number), None)

def show_menu():
    print('''Выберете действие: 
          1 - Показать доступные номера
          2 - Создать бронь
          3 - Отменить бронь
          4 - Выйти
          ''')