import ex1_hw5.ex1 as ex1
import ex1_hw5.ex2 as ex2
import ex1_hw5.ex3 as ex3

##### Ex1 passwd_validate tests

def test_ex1_passwd_less_6():
    assert ex1.password_validate("123df") == False

def test_ex1_passwd_has_passwd_lower():
    assert ex1.password_validate("123passwordfgddfg2") == False

def test_ex1_passwd_has_passwd_bigger():
    assert ex1.password_validate("1PaSSworDfgddfg2") == False

def test_ex1_passwd_only_numbers():
    assert ex1.password_validate("123456789") == False

def test_ex1_passwd_normal_passwd():
    assert ex1.password_validate("1123Ant384HGKdse") == True

##### Ex2 sum tests

def test_ex2_sum_integers():
    assert ex2.add([1, 2, 3, 4, 5]) == 15

def test_ex2_sum_floats():
    assert ex2.add([1.2, 2.2, 3.2, 4.2, 5.1]) == 15.9

def test_ex2_sum_int_and_floats():
    assert ex2.add([1, 2.2, 3, 4.2, 5]) == 15.4

def test_ex2_sum_str():
    assert ex2.add(["He", "ll", "o", "!"]) == None

def test_ex2_sum_empty_list():
    assert ex2.add([]) == 0

def test_ex2_sum_nothing():
    assert ex2.add(None) == None

##### Ex3 fibonacci tests

def test_ex3_fibonacci_5():
    assert ex3.fibonacci(5) == 5

def test_ex3_fibonacci_0():
    assert ex3.fibonacci(0) == None

def test_ex3_fibonacci_13():
    assert ex3.fibonacci(13) == 233

def test_ex3_fibonacci_str():
    assert ex3.fibonacci("str") == None