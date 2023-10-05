from datetime import datetime

from course import Courses
from student import Student

"""
    Grade Class

    Handles student's results for a single course

    Changelog:
        10JAN2023 - Initial release

"""
class Grades:
# [code, assessment[],semester, year]
    def __init__(self, code="", semester=1, assessment=[], year=0):
        self.code = code
        self.assessments = assessment # list of grades, up to 3
        self.semester = semester
        if year == 0:
           year = datetime.now().year
        self._year = year

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        if not value:
            raise ValueError
        self._code = value
        return self

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, value):
        if not value or value < 1 or value > 8:        
            raise ValueError
        self._semester = value
        return self

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not value:
            raise ValueError

        try:
            value = int(value)
        except:
            raise ValueError

        if not value in range(2022,2100):
            raise ValueError

        self._year = value
        return self

    @property
    def assessments(self):
        return list(self._assessment)

    @assessments.setter
    def assessments(self, value):
        if not value or len(value) > 3: #only allow 3 assessments       
            raise ValueError

        # do some range checking - uncomment for the unit testing
        #'''
        for v in value:
            if v < 0:
                raise ValueError("Results should be >= 0")
            if v > 100:
                raise ValueError ("Results should be <= 100")   
        #'''
        self._assessment = value
        return self

    def getAverage(self):
        l = len(self._assessment)
        s = sum(self._assessment)
        return s / l

    def getGrade(self):
        mark = self.getAverage()
        grade = 'ukn'
        if mark < 0 or mark > 100:
            return grade
        if mark >= 90:
            grade = 'A+'
        elif mark >= 85:
            grade = 'A'
        elif mark >= 80:
            grade = 'A-'
        elif mark >= 75:
            grade = 'B+'
        elif mark >= 70:
            grade = 'B'
        elif mark >= 65:
            grade = 'B-'
        elif mark >= 60:
            grade = 'C+'
        elif mark >= 55:
            grade = 'C'
        elif mark >= 50:
            grade = 'C-'
        elif mark >= 45:
            grade = 'D'
        elif mark < 45:
            grade = 'E'
        return grade

# this function cann be tested with a unit test
    def isPassing(self):
        if self.getAverage() > 49:
            return True
        else:
            return False

# this function cannot be tested with a unit test
    def isPassed(self):
        if self.getAverage() > 49:
            print("Is Passing")
        else:
            print ("Is not Passing")


    def show(self):
        return "\n".join([f"Code: {self.code}",
                          f"Semester: {self.semester}",
                          f"Year: {self.year}",
                          f"Marks: {self.assessments}",
                          f"Grade: {self.getGrade()} [{self.getAverage()}%]",
                          ])

    def __str__(self):
        return self.show()

# End of class, tests below
if __name__ == "__main__":
    print("Start Tests")
# Boundary range tests for the grade
# this test will fail - out of bounds check fail
    g = Grades("CS5100", 1, [-1,-1,-1])
    assert g.getAverage() == -1, "public methods"
    assert g.getGrade() == 'ukn', "public methods"

    g = Grades("CS5100", 1, [0,0,0])
    assert g.getAverage() == 0, "public methods"
    assert g.getGrade() == 'E', "public methods"
    
    g = Grades("CS5100", 1, [50,50,50])
    assert g.getAverage() == 50, "public methods"
    assert g.getGrade() == 'C-', "public methods"

    g = Grades("CS5100", 1, [100,100,100])
    assert g.getAverage() == 100, "public methods"
    assert g.getGrade() == 'A+', "public methods"

# this test will fail - out of bounds check fail
    g = Grades("CS5100", 1, [101,101,101])
    assert g.getAverage() == 101, "public methods"
    assert g.getGrade() == 'ukn', "public methods"

    try:
        g.semester = 9
    except ValueError:
        pass
    except:
        raise

    try:
        g.semester = 0
    except ValueError:
        pass
    except:
        raise

    print(g)
    print("End Tests")    