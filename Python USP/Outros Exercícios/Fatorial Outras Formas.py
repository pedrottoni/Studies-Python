def fatorial (n):
    f = n
    while n > 1:
        f = f * (n - 1)
        n = n - 1
    return (f)

def test_fatoria0():
    assert fatorial(0) == 1

def test_fatoria1():
    assert fatorial(1) == 1

def test_fatoriaNegativo():
    assert fatorial(-10) == 0

def test_fatoria5():
    assert fatorial(5) == 120

print(fatorial(1))