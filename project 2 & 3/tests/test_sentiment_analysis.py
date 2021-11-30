import sentiment_analysis as senti
import pytest

# test normally
def test_normal():
    argus = ['nice']
    assert senti(argus) == ['Positive']

# test with only digits
def test_digi():
    digi = ['123456'] * 100
    assert senti(digi) ==  pytest.raises(TypeError)
    
# test with only symbols
def test_symb():
    symb = ['!@#$%^&*'] * 100
    assert senti(symb) ==  pytest.raises(TypeError)
    
# test meaningless sentences
def test_no_meanning():
    no_meaning = ['jsalasda js sfakjfbkj cnsenkjnc,mnxzcnasd nasdasdn cnakjn,a sds']
    assert senti(no_meaning) == ['no meaning']
    
