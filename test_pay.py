from payment import calculate as cal

def test_cal(a,b):
    c = cal(a,b)

    test_c = a+b

    assert c == test_c

def test_divide(a, b):
    assert b == 0



test(10,20)
test(1,15)
test(40,150)

z = divide(21,3)
a = divide(21,0)