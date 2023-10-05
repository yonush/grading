"""
    Course Class

    Handles all of the course related information
    
    Changelog:
        10JAN2023 - Initial release
"""


class Courses:
    # course code, description, level, credits, weights
    _COURSES = {
        "CS5100": ["Computer System Architecture", 5, 15, [30, 30, 40]],
        "PF5110": ["Programming Fundamentals", 5, 15, [30, 30, 40]],
        "CT5120": ["Concepts & Tools", 5, 15, [30, 30, 40]],
        "WD5130": ["Website Development", 5, 15, [30, 30, 40]],
        "UX5210": ["UX and UI fundamental", 5, 15, [30, 30, 40]],
        "DT5220": ["Intro to Data Concepts", 5, 15, [30, 30, 40]],
        "PM5240": ["Agile Projects", 5, 15, [30, 30, 40]],
        "IS5450": ["Information Systems", 5, 15, [30, 30, 40]],
        "PR5510": ["Intro to OO Programming", 5, 15, [30, 30, 40]],
        "AW6100": ["Automation and Embedded Systems", 6, 15, [30, 30, 40]],
        "DB6200": ["Database Management Systems", 6, 15, [30, 30, 40]],
        "DC6210": ["Data Communications & Networking", 6, 15, [30, 30, 40]],
        "HW6230": [
            "Electronics and Internet of Things Technology",
            6,
            15,
            [30, 30, 40],
        ],
        "MA6240": ["Maths in IT", 6, 15, [30, 30, 40]],
        "NA6250": ["Advanced Networking and the Cloud", 6, 15, [30, 30, 40]],
        "PM6310": ["Project Management", 6, 15, [30, 30, 40]],
        "SD6340": ["Systems Analysis & Design", 6, 30, [30, 30, 40]],
        "PR6350": ["User Experience & User Interfaces", 6, 15, [30, 30, 40]],
        "KM6390": ["Knowledge Management", 6, 15, [30, 30, 40]],
        "WD6400": ["Adv. Internet and Web Page Development", 6, 15, [30, 30, 40]],
        "PR6500": ["Advanced OO Programming", 6, 15, [30, 30, 40]],
        "PR6510": ["Enterprise Software Development", 6, 15, [30, 30, 40]],
        "OS6600": ["Operating Systems", 6, 15, [30, 30, 40]],
        "DF6100": ["Digital Forensics Fundamentals", 6, 15, [30, 30, 40]],
        "AI7110": ["Machine Learning and Artificial Intelligence", 7, 15, [30, 30, 40]],
        "FM7120": ["Mechatronics in IT", 7, 15, [30, 30, 40]],
        "HW7230": ["Enterprise Support and Infrastructure", 7, 15, [30, 30, 40]],
        "DA7240": ["Data Analytics", 7, 15, [30, 30, 40]],
        "WD7350": ["Web Application Programming", 7, 15, [30, 30, 40]],
        "PJ7390": ["Project or Internship", 7, 15, [30, 30, 40]],
        "EC7390": ["E-Business Strategies", 7, 15, [30, 30, 40]],
        "ST7400": ["Special Topic", 7, 15, [30, 30, 40]],
        "IM7450": ["Info Tech Mgmt & Professionalism", 7, 15, [30, 30, 40]],
        "PR7500": ["Business Application Programming", 7, 15, [30, 30, 40]],
        "SY7660": ["Information Security", 7, 15, [30, 30, 40]],
        "GA7100": ["GIS Analytics", 7, 15, [30, 30, 40]],
        "CP7001": ["Capstone", 7, 60, [30, 30, 40]],
    }

    # Public Class methods
    # Constructor
    def __init__(self):
        super().__init__()

    @classmethod
    def getCourses(cls):
        return cls._COURSES

    @classmethod
    def courseCodes(cls):
        return list(cls._COURSES.keys())

    @classmethod
    def validCourse(cls, value):
        if not value or len(value) != 6:
            return False
        try:
            if cls._COURSES[value]:
                return True
        except:
            return False
        return True

    @classmethod
    def getCourse(cls, value):
        if not cls.validCourse(value):
            raise ValueError
        return cls._COURSES[value]

    @classmethod
    def getCoursename(cls, value):
        if not cls.validCourse(value):
            raise ValueError
        return cls._COURSES[value][0]

    @classmethod
    def getLevel(cls, value):
        if not cls.validCourse(value):
            raise ValueError
        return cls._COURSES[value][1]

    @classmethod
    def getCredits(cls, value):
        if not cls.validCourse(value):
            raise ValueError
        return cls._COURSES[value][2]

    @classmethod
    def getWeights(cls, value):
        if not cls.validCourse(value):
            raise ValueError
        return cls._COURSES[value][3]

    @classmethod
    def add(cls, code="", name="", level=-1, credits=15, weights=[30, 30, 40]):
        if not code or not name or not level or not credits or not weights:
            raise ValueError

        if len(code) != 6:
            return ValueError

        # validate course level
        try:
            level = int(level)
        except:
            raise ValueError
        if level not in [5, 6, 7]:
            raise ValueError("Level should be 5,6 or 7")

        # validate course credits
        try:
            credits = int(credits)
        except:
            raise ValueError
        if credits not in [15, 30, 45, 60]:
            raise ValueError("Credits should be 15,30,45 or 60")

        # validate course weights
        if len(weights) != 3:
            raise ValueError

        for i in range(3):
            try:
                weights[i] = int(weights[i])
            except:
                raise ValueError
        if weights[0] + weights[1] + weights[2] != 100:
            raise ValueError("Sum of weigths should be 100")

        course = [name, level, credits, weights]
        cls._COURSES[code] = course

    @classmethod
    def remove(cls, code):
        if not cls.validCourse(code):
            raise ValueError
        del cls._COURSES[code]

    def __str__(self):
        return f"{self._COURSES}"

    def __repr__(self):
        return f"{type(self).__name__}()"

    def reload(cls):
        _COURSES = {
            "CS5100": ["Computer System Architecture", 5, 15, [30, 30, 40]],
            "PF5110": ["Programming Fundamentals", 5, 15, [30, 30, 40]],
            "CT5120": ["Concepts & Tools", 5, 15, [30, 30, 40]],
            "WD5130": ["Website Development", 5, 15, [30, 30, 40]],
            "UX5210": ["UX and UI fundamental", 5, 15, [30, 30, 40]],
            "DT5220": ["Intro to Data Concepts", 5, 15, [30, 30, 40]],
            "PM5240": ["Agile Projects", 5, 15, [30, 30, 40]],
            "IS5450": ["Information Systems", 5, 15, [30, 30, 40]],
            "PR5510": ["Intro to OO Programming", 5, 15, [30, 30, 40]],
            "DF6100": ["Digital Forensics Fundamentals", 6, 15, [30, 30, 40]],
            "AW6100": ["Automation and Embedded Systems", 6, 15, [30, 30, 40]],
            "DB6200": ["Database Management Systems", 6, 15, [30, 30, 40]],
            "DC6210": ["Data Communications & Networking", 6, 15, [30, 30, 40]],
            "HW6230": [
                "Electronics and Internet of Things Technology",
                6,
                15,
                [30, 30, 40],
            ],
            "MA6240": ["Maths in IT", 6, 15, [30, 30, 40]],
            "NA6250": ["Advanced Networking and the Cloud", 6, 15, [30, 30, 40]],
            "PM6310": ["Project Management", 6, 15, [30, 30, 40]],
            "SD6340": ["Systems Analysis & Design", 6, 30, [30, 30, 40]],
            "PR6350": ["User Experience & User Interfaces", 6, 15, [30, 30, 40]],
            "KM6390": ["Knowledge Management", 6, 15, [30, 30, 40]],
            "WD6400": ["Adv. Internet and Web Page Development", 6, 15, [30, 30, 40]],
            "PR6500": ["Advanced OO Programming", 6, 15, [30, 30, 40]],
            "PR6510": ["Enterprise Software Development", 6, 15, [30, 30, 40]],
            "OS6600": ["Operating Systems", 6, 15, [30, 30, 40]],
            "AI7110": [
                "Machine Learning and Artificial Intelligence",
                7,
                15,
                [30, 30, 40],
            ],
            "FM7120": ["Mechatronics in IT", 7, 15, [30, 30, 40]],
            "HW7230": ["Enterprise Support and Infrastructure", 7, 15, [30, 30, 40]],
            "DA7240": ["Data Analytics", 7, 15, [30, 30, 40]],
            "WD7350": ["Web Application Programming", 7, 15, [30, 30, 40]],
            "PJ7390": ["Project or Internship", 7, 15, [30, 30, 40]],
            "EC7390": ["E-Business Strategies", 7, 15, [30, 30, 40]],
            "ST7400": ["Special Topic", 7, 15, [30, 30, 40]],
            "IM7450": ["Info Tech Mgmt & Professionalism", 7, 15, [30, 30, 40]],
            "PR7500": ["Business Application Programming", 7, 15, [30, 30, 40]],
            "SY7660": ["Information Security", 7, 15, [30, 30, 40]],
            "GA7100": ["GIS Analytics", 7, 15, [30, 30, 40]],
            "CP7001": ["Capstone", 7, 60, [30, 30, 40]],
        }

        cls._COURSES.clear()
        cls._COURSES.update(_COURSES)


# End of class, tests below
if __name__ == "__main__":
    print("Start Tests")
    C = Courses()
    print(C)  # __str__

    assert C.getCourse("SY7660") == [
        "Information Security",
        7,
        15,
        [30, 30, 40],
    ], "Public methods - getCourse"

    assert (
        C.getCoursename("SY7660") == "Information Security"
    ), "Class methods - getCoursename"
    assert C.getLevel("SY7660") == 7, "Class methods - getLevel"
    assert C.getCredits("SY7660") == 15, "Class methods - getCredits"
    assert C.getWeights("SY7660") == [30, 30, 40], "Class methods - getWeights"

    C.add("AB1234", "Test Course", 5, 15, [33, 33, 34])

    assert C.getCoursename("AB1234") == "Test Course", "Class methods - getCoursename"
    assert C.getLevel("AB1234") == 5, "Class methods - getLevel"
    assert C.getCredits("AB1234") == 15, "Class methods - getCredits"
    assert C.getWeights("AB1234") == [33, 33, 34], "Class methods - getWeights"

    C.remove("AB1234")

    try:
        assert (
            C.getCoursename("AB1234") == "Information Security"
        ), "Class methods - getCourse"
    except ValueError:
        pass
    except:
        raise

    # print(C.courseCodes())
    print("End Tests")
