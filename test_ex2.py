import hw3_new.ex1 as ex1

# Сначала создадим тесты проверки доп функции проверки ходов

def test_ex1_move_check_2():
    assert ex1.move_check(2) == 2

def test_ex1_move_check_0():
    assert ex1.move_check(0) == 0

def test_ex1_move_check_minus_1():
    assert ex1.move_check(-1) == 0

def test_ex1_move_check_str():
    assert ex1.move_check("str") == 0

# Далее проверим главную функцию, проверка корректности
# для всех направлений не требуется т.к. проверили
# под функцию.

def test_ex1_move_forward_3():
    assert ex1.move([0, 0], '1', 3) == [3, 0]

def test_ex1_move_forward_minus_1():
    assert ex1.move([0, 0], '1', -1) == [0, 0]

def test_ex1_move_forward_str():
    assert ex1.move([0, 0], '1', "str") == [0, 0]

def test_ex1_move_forward_0():
    assert ex1.move([0, 0], '1', 0) == [0, 0]

def test_ex1_move_backward_0():
    assert ex1.move([0, 0], '2', 3) == [-3, 0]

def test_ex1_move_right_0():
    assert ex1.move([0, 0], '3', 3) == [0, 3]

def test_ex1_move_left_0():
    assert ex1.move([0, 0], '4', 3) == [0, -3]
    