from main import product

def test_product_basico():
    assert product([1,2,3,4]) == 24
    assert product([5,0,2]) == 0
    assert product([7]) == 7
