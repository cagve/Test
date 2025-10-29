from mean import mean

def test_media_basica():
    assert mean([1, 2, 3, 4, 5]) == 3

def test_media_negativos():
    assert mean([-1, -2, -3, -4]) == -2.5

def test_media_decimales():
    assert mean([1, 2, 2]) == 5 / 3  # Esto falla en Python 2 (5/3 == 1)

