import pytest
@pytest.mark.smoke
def test_simple():
    assert 1+1 == 2
@pytest.mark.regression
def test_simple2():
    assert 1+3 == 4
@pytest.mark.skip
def test_assertcompare():
    x=4
    y=4
    assert x==y
@pytest.mark.skipif
def test_demo():
    print("skip if")
@pytest.mark.xfail
def test_assertnotequal():
    x=4
    y=5
    assert x!=y
@pytest.mark.xfail
def test_sample4():
    a="shobs"
    b="shobs"
    assert a.__eq__(b)
