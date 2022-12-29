
def fibonacci(n):
    """Функция вычисления чисел Фибоначчи
    args:
        n - номер числа Фибоначчи
    returns:
        Число Фибоначчи по номеру n
        None, если число меньше 1
        None, если введено не число
    """
    try:
        if n < 1:
            return None
        elif n in (1, 2):
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    except (ValueError, TypeError):
        return None
   
    
