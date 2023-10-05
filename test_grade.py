from grade import Grades
import pytest # used for unit tests
'''
    https://docs.pytest.org/en/latest/contents.html
    pip install -U pytest
    pytest --version
    pytest
    pytest -q test_grade.py
    pytest --fixtures

    https://coverage.readthedocs.io/en/6.4.4/
    pip install pytest-cov
    
    coverage run -m pytest

'''
# ?% code coverage - some functionas tested
# all three functions are tested

# -----------TEST AVERAGE -------------
class TestAverage:
    grade = Grades("CS5100", 1,[0,0,0] )
    
    def test_average1(self):
        self.grade.assessments = [0,0,0]
        assert self.grade.getAverage() == 0

    def test_average2(self):
        self.grade.assessments = [50,50,50]
        assert self.grade.getAverage() == 50

    def test_average3(self):
        self.grade.assessments = [100,100,100]
        assert self.grade.getAverage() == 100

    # remove the comments in the grade.assessments function for the 
    # range checking
    def test_average4(self):
        with pytest.raises(ValueError):
            self.grade.assessments = [-1,-1,-1]        
            assert self.grade.getAverage() == -1

    def test_average5(self):
        with pytest.raises(ValueError):
            self.grade.assessments = [101,101,101]
            assert self.grade.getAverage() == 101   

    @pytest.mark.skip(reason="This test will fail if run")
    def test_average6(self):
        # results should be values not letters
        self.grade.assessments = ['A','B','C']
        assert self.grade.getAverage() == -1

# this execution should not really happen but the 
# div/0 was commented in function for showing how to test for exceptions
@pytest.mark.skip(reason="This test will fail if run")
def test_exceptions():    
    g = Grades("CS5100", 1,[])    
    with pytest.raises(ZeroDivisionError):
        g.getAverage()    

# -----------TEST GRADE -------------
# this is a 100% branch test - testing each branch of the if...else...
# note this should really be individual tests grouped 
class TestGrade:
    grade = Grades("CS5100", 1,[0,0,0] )
    def testAplus(self):
        self.grade.assessments = [95,95,95]
        assert self.grade.getGrade() == 'A+'

    def testA(self):
        self.grade.assessments = [85,85,85]
        assert self.grade.getGrade() == 'A'

    def testAminus(self):
        self.grade.assessments = [80,80,80]
        assert self.grade.getGrade() == 'A-'

# remainder of the coverage tests left for you to do
    def testE(self):        
        self.grade.assessments = [0,0,0]
        assert self.grade.getGrade() == 'E'

@pytest.mark.skip(reason="This test wont work because poorly written function")
def test_passing():
    # ???, not a valid test, function does not return anything!
    # how do we test this function? It should be refactored.
    g = Grades("CS5100", 1, [10,10,10])
    assert g.ispassed() == None
	
