import pytest
from main import is_perfect

@pytest.mark.parametrize("numero", [6, 28, 496, 8128])
def test_numeros_perfectos(numero):
    assert is_perfect(numero)

@pytest.mark.parametrize("numero", [1, 2, 3, 4, 5, 7, 10, 12, 20, 100])
def test_numeros_no_perfectos(numero):
    assert not is_perfect(numero)

@pytest.mark.parametrize("numero", [0, -1, -6, -28])
def test_valores_invalidos(numero):
    with pytest.raises(ValueError):
        is_perfect(numero)
