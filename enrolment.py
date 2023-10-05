from student import Student
from course import Courses
from grade import Grades

"""
    Enrolment Class

    Handles student's Enrolment & grades for courses by semester 

    Changelog:
        10JAN2023 - Initial release


"""
class Enrolment:

    # Constructor
    def __init__(self,student,grades):
        self._student = student
        self._grades = grades # [list of Grades]

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, value):
        if not value:
            raise ValueError
        self._student = value
        return self

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, value):
        if not value:
            raise ValueError
        self._grades = value
        return self

    # Public methods
    def addCourse(self,value):
        if not value: # add check for valid course code
            raise ValueError 

        self._grades.append(value)

    def removeCourse(self,value):
        if not value: # add check for valid course code
            raise ValueError 
        for i in range(len(self._grades)):
           if self._grades[i].code == value:
            del self._grades[i]
            break


    def getCourses(self):
        return list(map(lambda x: x.code,self._grades))

    def getMarks(self,code):
        if not code: # add check for valid course code
            raise ValueError
        '''
        for g in self._grades:
            if g.code == code:
                return g.assessments    
        '''  
        g = list(map(lambda g: g.assessments, filter(lambda g: g.code == code, self._grades)))          
        return g[0]

    def getGrade(self,code):
        if not code: # add check for valid course code
            raise ValueError
        for g in self._grades:
            if g.code == code:
                return g.getGrade()    
        return "ukn"
 
    def findAssessByCode(self,code):
        if not code: 
            raise ValueError
        for g in self._grades:
            if g.code == code:
                return g
        return None
        
    def getAverage(self,code):
        if not code: # add check for valid course code
            raise ValueError
        for g in self._grades:
            if g.code == code:
                return g.getAverage()    
        return 0

    def showMarks(self):
        s = "\n"
        for g in self._grades:
            s = s + f"{g.code} {g.semester}:{g.assessments}\n"
        return s

    def showGrades(self):
        s = ""
        for g in self._grades:
            s = s + f"{g.code}: {g.getGrade()} [{g.getAverage()}%]\n"
        return s

    def show(self):
        return "\n".join([f"Student ID: {self.student.studentid}",
                          f"Student: {self.student.name}",
                          f"Grades: \n{self.showGrades()}",
                          ])

    def __str__(self):
        return self.show()

# End of class, tests below
if __name__ == "__main__":
    print("Start Tests")

    s = Student(20220001,"Joe Bloggs", "021-123-1234", "joe.bloggs@mail.com")

    g = [Grades("CS5100", 1, [50,50,50]),
         Grades("PF5110", 1, [60,60,60]),
         Grades("CT5120", 1, [70,70,70]),
         Grades("WD5130", 1, [80,80,80])]

    e = Enrolment(s,g)

    assert e.showMarks() == "\nCS5100 1:[50, 50, 50]\nPF5110 1:[60, 60, 60]\n"\
                            "CT5120 1:[70, 70, 70]\nWD5130 1:[80, 80, 80]\n",\
                            "Public methods - allMarks"    
    assert e.showGrades() == "CS5100: C- [50.0%]\nPF5110: C+ [60.0%]\n"\
                            "CT5120: B [70.0%]\nWD5130: A- [80.0%]\n",\
                            "Public methods - allGrades"    
    assert e.getMarks("CS5100") == [50,50,50 ], "Public methods - getMarks"   
    assert e.getGrade("CS5100") == "C-", "Public methods - getGrade"   
    assert e.getAverage("CS5100") == 50, "Public methods - getAverage"   
    
    e.addCourse(Grades("UX5210", 1, [65,65,65]))
    assert e.getMarks("UX5210") == [65,65,65 ], "Public methods - getMarks"   
    assert e.getGrade("UX5210") == "B-", "Public methods - getGrade"   
    assert e.getAverage("UX5210") == 65, "Public methods - getAverage"
    assert e.getCourses() == ['CS5100', 'PF5110', 'CT5120', 'WD5130', 'UX5210'], "Public methods - getCourses"   
    e.removeCourse('UX5210')
    assert e.getCourses() == ['CS5100', 'PF5110', 'CT5120', 'WD5130'], "Public methods - getCourses"   
    
    a = e.findAssessByCode('CS5100')    
    assert a.assessments == [50, 50, 50], "Public methods - findAssessByCode"   

    #print(e.grades[0].code)
    print("End Tests")
