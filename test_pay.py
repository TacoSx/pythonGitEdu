from payment import calculate as cal
from payment import calculate as divide

def test_cal(a,b):
    c = cal(a,b)

    test_c = a+b

    assert c == test_c

def test_divide(a, b):
    assert b == 0
    c = divide(a,b)




test_cal(10,20)
test_cal(1,15)
test_cal(40,150)

divide(21,3)
divide(21,0)