from course import Courses
from enrolment import Enrolment
from student import Student

"""

    Enrolments are stored in a private dict _cohort, keyed by student id
    Changelog:
        28NOV2022 - Initial release

"""


def group_by(seqs, idx=0, merge=True):
    d = dict()
    for seq in seqs:
        k = seq[idx]
        v = d.get(k, tuple()) + (
            seq[:idx] + seq[idx + 1 :] if merge else (seq[:idx] + seq[idx + 1 :],)
        )
        d.update({k: v})
    return d


class School:
    # Public Methods
    def __init__(self):
        self._cohort = {}
        self._courses = Courses()

    # class instance properties
    @property
    def courses(self):
        return self._courses

    @property
    def cohort(self):
        return self._cohort

    @property
    def allstudent(self):
        return list(self._cohort.values())

    @property
    def studentids(self):
        return sorted(list(self._cohort.keys()))

    # public methods
    def clear(self):
        self._cohort.clear()
        return self

    def add(self, enroll):
        if not enroll:
            raise ValueError
        if not isinstance(enroll, Enrolment):
            raise TypeError

        self._cohort[int(enroll.student.studentid)] = enroll
        return self

    def remove(self, ID):
        if not ID or not self._cohort[ID]:
            raise ValueError
        del self._cohort[ID]
        return self

    def allStudentNames(self):
        l = map(lambda m: m.student.name, list(self._cohort.values()))
        return list(l)

    def findStudent(self, ID) -> Student:
        if not ID:
            raise ValueError
        if ID in list(self._cohort):
            return self._cohort[ID]
        return None

    def findStudentByname(self, name) -> Student:
        if not name:
            raise ValueError
        for s in list(self._cohort.values()):
            if s.student.name == name:
                return s
        return None

    def findAssessByCode(self, ID, code):
        if not code or not ID:
            raise ValueError
        if ID in list(self._cohort):
            return self._cohort[ID].findAssessByCode(code)
        return None

    def updAssessByID(self, ID, assess):
        if not assess or not ID:
            raise ValueError
        if ID in list(self._cohort):
            g = self._cohort[ID].grades
            for i in range(len(g)):
                if g[i].code == assess.code:
                    self._cohort[ID].grades[i] = assess

    def addAssessByID(self, ID, assess):
        if not assess or not ID:
            raise ValueError
        if ID in list(self._cohort):
            g = self._cohort[ID]
            if not assess.code in g.getCourses():
                self._cohort[ID].addCourse(assess)

    def getCoursesByid(self, ID):
        if not ID:
            raise ValueError
        if ID in list(self._cohort):
            g = self._cohort[ID]
            return g.getCourses()
        return None

    def showGradesByid(self, ID):
        if not ID:
            raise ValueError
        if ID in list(self._cohort):
            s = self._cohort[ID]
            return str(s.showGrades())
        return None

    # course related
    def studentsByCourse(self, code):
        return [
            (c.student.studentid)
            for c in list(self._cohort.values())
            if code in c.getCourses()
        ]

    def show(self):
        s = ""
        for c in list(self._cohort.values()):
            s += "\n".join(
                [
                    f"Student ID: {c.student.studentid}",
                    f"Student name: {c.student.name}",
                    f"Courses: {c.getCourses()}\n",
                ]
            )
        return s

    def __str__(self):
        return self.show()


# End of class, tests below
if __name__ == "__main__":
    from student import Student
    from course import Courses
    from grade import Grades
    import pprint

    pp = pprint.PrettyPrinter(indent=4)
    print("Start Tests")

    school = School()
    students = [
        Student(20220001, "Joe Bloggs", "021-123-1234", "joe.bloggs@mail.com"),
        Student(20220002, "Sue Black", "021-123-1234", "sue.black@mail.com"),
        Student(20220003, "Jane Doe", "021-123-1234", "jane.doe@mail.com"),
        Student(20220004, "Kate White", "021-123-1234", "kate.white@mail.com"),
    ]

    grades = [
        Grades("CS5100", 1, [50, 50, 50]),
        Grades("PF5110", 1, [60, 60, 60]),
        Grades("CT5120", 1, [70, 70, 70]),
        Grades("WD5130", 1, [80, 80, 80]),
        Grades("UX5210", 1, [65, 65, 65]),
    ]

    # populate the school with Enrolments
    for s in students:
        e = Enrolment(s, grades)
        school.add(e)

    s = school.findStudent(20220002)
    assert int(s.student.studentid) == 20220002, "Public methods - findStudentByID"

    s = school.findStudentByname("Jane Doe")
    assert int(s.student.studentid) == 20220003, "Public methods - findStudentByname"

    b = school.studentsByCourse("CS5100")
    assert b == [
        20220001,
        20220002,
        20220003,
        20220004,
    ], "Public methods - studentsByCourse"

    g = school.getCoursesByid(20220001)
    assert g == [
        "CS5100",
        "PF5110",
        "CT5120",
        "WD5130",
        "UX5210",
    ], "Public methods - getCoursesByid"

    a = school.findAssessByCode(20220001, "CS5100")
    assert a.assessments == [50, 50, 50], "Public methods - findAssessByCode"

    s = Student(20220001, "Joe Bloggs", "021-123-1234", "joe.bloggs@mail.com")
    school.cohort[20220001].student = s

    school.remove(20220004)
    b = school.studentsByCourse("CS5100")
    assert b == [20220001, 20220002, 20220003], "Public methods - studentsByCourse"

    # print(school.cohort[20220001])
    # print(school.allStudentNames())
    # print(school.showGradesByid(20220001))
    # print(school.findAssessByCode(20220001,'CS5100'))
    # print(school)
    print("End Tests")
# End of class, tests below
