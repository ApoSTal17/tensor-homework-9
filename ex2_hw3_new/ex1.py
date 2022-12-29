
def move(coord, direction, amount):
    """Функция изменяет координаты в соответствии
    с направлением и количеством шагов

    args:
        coord - [x, y] список
        direction - числа:
            1 - вперед
            2 - назад
            3 - вправо
            4 - влево
        amount - число шагов, целое
    returns:
        [x, y] список с измененными координатами
        None, если неверный формат списка, направления
    """
    if (type(coord) == list 
        and type(coord[0]) == (int or float) 
        and type(coord[1]) == (int or float)):

        match direction:
                case '1':
                    coord[0] += move_check(amount)
                case '2':
                    coord[0] -= move_check(amount)
                case '3':
                    coord[1] += move_check(amount)
                case '4':
                    coord[1] -= move_check(amount)
                case _:
                    return None
        return coord
    else:
        return None
        
    

def move_check(amount):
    """Функция получает количество ходов и проверяет это число
    args:
        amount - целое число
    returns:
        Целое число ходов.
        0, если пользователь ошибся или неправильно ввел число
    """
    try:
        if amount >= 0:
            return amount
        else:
            return 0
    except (ValueError, TypeError):
        return 0