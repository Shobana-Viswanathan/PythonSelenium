import pytest
def test_sample_one():
    print("Hai")
def test_sample1():
    print("Welcome")
def test_sample2():
    print("Pytest")
def test_simple():
    assert 1+1 == 2
def test_simple2():
    assert 1+3 == 4
def test_assertcompare():
    x=4
    y=4
    assert x==y
def test_assertnotequal():
    x=4
    y=5
    assert x!=y
def test_assertin():
    num=[1,2,3,4]
    assert 3 in num
def test_sample4():
    a="arun"
    b="arun"
    assert a.__eq__(b)

    