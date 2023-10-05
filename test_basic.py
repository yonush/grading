import pytest # used for the unit tests
from grade import Grades

def test_average1():
    g = Grades("CS5100", 1, [-1,-1,-1])
    assert g.getAverage() == -1, "public methods"

def test_average2():
    g = Grades("CS5100", 1, [0,0,0])
    assert g.getAverage() == 0, "public methods"

def test_average3():
    g = Grades("CS5100", 1, [50,50,50])
    assert g.getAverage() == 50, "public methods" 

def test_average4():
    g = Grades("CS5100", 1, [100,100,100])
    assert g.getAverage() == 100, "public methods" 

def test_average5():
    g = Grades("CS5100", 1, [101,101,101])
    assert g.getAverage() == 101, "public methods"    