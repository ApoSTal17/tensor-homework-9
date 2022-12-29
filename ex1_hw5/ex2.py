def add(args):
    """Функция суммирования любого количества численных аргументов
    
    args:
        args - численные аргументы в любом количестве в виде списка или кортежа
    returns:
        Численную сумму аргументов args
    """
    try:
        value = sum(args)
    except (TypeError, ValueError):
        return None
    return value
