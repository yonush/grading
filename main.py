"""
GradeAce results system

    Known limitations:
    - The GUI framework is limited in the finer controls and available configuration
    - Unit test coverage is limited - function/class level only. 
    - Error handling could be better. 
    - Main program logic is messy. 
    - Course administration is broken with the weights
    - Grade/Enrolment administration could handled better
    - Code commentary is sparse
    - Not all class functionality is exposed in the GUI.

    - Grading data is NOT persistent - changes are not recorded to offline storage

    colors: https://wiki.tcl-lang.org/page/Color+Names%2C+running%2C+all+screens

    Changelog:
        10JAN2023 - Initial release

    # https://lawsie.github.io/guizero/
"""

import pathlib
from guizero import (App, Box, Combo, ListBox, Picture, PushButton, Text,
                     TextBox, TitleBox, Window)

from course import Courses
from enrolment import Enrolment
from grade import Grades

from school import School
from student import Student


############# public declarations ##############
pwd = pathlib.Path().absolute()  # current working folder

school = School()
_studentid = None  # currenly selected student
_coursecode = None  # currently selected course

app = App(title="GradeAce Results System",
          width=800, height=600, bg="skyblue3")
app.text_color = "black"
main_box = Box(app, height="fill", width="fill", align="left", border=False)
heading_box = Box(main_box, width="fill", align="top", border=False, layout="grid")
Picture(heading_box, image=f"{pwd}/static/logo2.png", align="left", grid=[0,0])
heading_text = Text(heading_box, size=25, text="Results System", grid=[1,0])

# this is a placeholder event handler
def evtNull(value=None):
    # null event placeholder
    pass


def refreshLists():
    global _studentid, _coursecode, _enrollcode

    studentList.clear()
    Student_select.clear()
    for s in school.allStudentNames():
        studentList.append(s)
        Student_select.append(s)
    s = school.findStudentByname(studentList.items[0])
    _studentid = s.student.studentid

    courseList.clear()
    course1List.clear()
    for c in school.courses.courseCodes():
        d = school.courses.getCoursename(c)
        courseList.append(f"{c} - {d}")
        course1List.append(f"{c} - {d}")
    c = courseList.items[0]
    _coursecode = c.split()[0]

    assessList.clear()
    enrollList.clear()
    for g in school.getCoursesByid(_studentid):
        assessList.append(g)
        enrollList.append(g)
    _enrollcode = enrollList.items[0]

# load the first student's details using name as the key
    evtUpdateDetails(school.allstudent[0].student.name)

############# Student maintenance  ##############

## -----local events for student maintenance ------------ ##


def evtStudentHide():
    frmStudent.hide()


def displayStudent(value):
    global _studentid

    s = school.findStudentByname(value)
    if s != None:
        edID.value = s.student.studentid
        edName.value = s.student.name
        edContact.value = s.student.contact
        edEmail.value = s.student.email
        _studentid = s.student.studentid


def evtDeleteStudent():
    global _studentid

    s = school.findStudent(_studentid)
    if s != None:
        school.remove(_studentid)
        refreshLists()
        displayStudent(studentList.items[0])


def evtUpdateStudent():
    global _studentid

    s = school.findStudent(_studentid)
    if s != None:
        s = Student(_studentid, edName.value, edContact.value, edEmail.value)
        school.cohort[_studentid].student = s
        refreshLists()


def evtAddStudent():
    global _studentid

    c = school.findStudent(_studentid)
    if c == None:  # make sure it does not exist
        s = Student(_studentid, edName.value, edContact.value, edEmail.value)
        school.cohort[_studentid].student = s
        school.cohort[_studentid].grades = []
        edID.value = ""
        edName.value = ""
        edContact.value = ""
        edEmail.value = ""
        refreshLists()
        displayStudent(studentList.items[0])


## ----- Student form/window ------------ ##
frmStudent = Window(app, title="Student Maintenance", width=400,
                    height=400, layout="auto", bg="skyblue3")
frmStudent.hide()
Text(frmStudent, size=24, text="Student Maintenance")

studbox = Box(frmStudent, width="fill", align="top",
              border=True, layout="auto")
_students = []
studentList = ListBox(studbox, items=_students, height='fill', width='fill',
                      multiselect=False, command=displayStudent, scrollbar=True)
studentList.bg = "cornsilk2"
studbox = Box(frmStudent, width="fill", align="top",
              border=True, layout="grid")
Text(studbox, text="ID:", grid=[0, 0])
Text(studbox, text="Name:", grid=[0, 1])
Text(studbox, text="Contact:", grid=[0, 2])
Text(studbox, text="Email:", grid=[0, 3])

edID = TextBox(studbox, text="", width=25, align="left", grid=[1, 0])
edName = TextBox(studbox, text="", width=25, align="left", grid=[1, 1])
edContact = TextBox(studbox, text="", width=25, align="left",  grid=[1, 2])
edEmail = TextBox(studbox, text="", width=50, align="left",  grid=[1, 3])
edID.bg = "cornsilk2"
edName.bg = "cornsilk2"
edContact.bg = "cornsilk2"
edEmail.bg = "cornsilk2"

btnbox = Box(frmStudent, width="fill", align="top", border=True, layout="auto")
btn = PushButton(btnbox, text="New", command=evtAddStudent, align="left")
btn.bg = "skyblue1"
btn = PushButton(btnbox, text="Update", command=evtUpdateStudent, align="left")
btn.bg = "skyblue1"
btn = PushButton(btnbox, text="Delete", command=evtDeleteStudent, align="left")
btn.bg = "skyblue1"
btn = PushButton(btnbox, text="Cancel", command=evtStudentHide, align="left")
btn.bg = "skyblue1"

############# Course selection maintenance  ##############

## -----local events for Course selection maintenance ------------ ##
_enrollcode = None


def evtEnrollHide():
    frmEnroll.hide()


def displayEnrollLeft(value):
    global _coursecode
    _coursecode = value.split()[0]


def displayEnrollRight(value):
    global _enrollcode
    _enrollcode = value


def evtDeleteEnroll():
    global _studentid, _enrollcode

    s = school.findStudent(_studentid)
    if s != None:
        s.removeCourse(_enrollcode)
        refreshLists()


def evtAddEnroll():
    global _studentid,  _coursecode

    c = school.findStudent(_studentid)
    if c != None:  # make sure it does not exist
        school.addAssessByID(_studentid, Grades(
            _coursecode, assessment=[0, 0, 0]))
        refreshLists()


## ----- Student form/window ------------ ##
frmEnroll = Window(app, title="Student Maintenance", width=400,
                   height=400, layout="auto", bg="skyblue3")
frmEnroll.hide()
Text(frmEnroll, size=24, text="Student Maintenance")

studbox = Box(frmEnroll, width="fill", align="top", border=True, layout="auto")
_Courses = []
course1List = ListBox(studbox, items=_Courses, height='fill', width='fill',
                      multiselect=False, command=displayEnrollLeft, scrollbar=True)
course1List.bg = "cornsilk2"

_Enroll = []
enrollList = ListBox(studbox, items=_Enroll, height='fill', width='fill',
                     multiselect=False, command=displayEnrollRight, scrollbar=True)
enrollList.bg = "cornsilk2"

btnbox = Box(frmEnroll, width="fill", align="top", border=True, layout="auto")
btn = PushButton(btnbox, text="Add Course", command=evtAddEnroll, align="left")
btn.bg = "skyblue1"
btn = PushButton(btnbox, text="Remove Course",
                 command=evtDeleteEnroll, align="left")
btn.bg = "skyblue1"
btn = PushButton(btnbox, text="Close", command=evtEnrollHide, align="left")
btn.bg = "skyblue1"

############# Student assessment maintenance  ##############

## -----local events for student assessment maintenance ------------ ##
# [code, assessment[],semester, year]


def evtAssessHide():
    frmAssess.hide()


def displayAssess(value):
    global _studentid, _coursecode

    g = school.findAssessByCode(_studentid, value)
    if g != None:
        edCrsCode.value = g.code
        edSemester.value = g.semester
        edYear.value = g.year
        edAssess1.value = g.assessments[0]
        edAssess2.value = g.assessments[1]
        edAssess3.value = g.assessments[2]
        _coursecode = g.code


def evtUpdateAssess():
    global _studentid

    s = school.findStudent(_studentid)
    if s != None:
        m = [int(edAssess1.value), int(edAssess2.value), int(edAssess3.value)]
        g = Grades(edCrsCode.value, edSemester.value, m, edYear.value)
        school.updAssessByID(_studentid, g)
        refreshLists()
        displayAssess(assessList.items[0])


## ----- Assessment form/window ------------ ##
frmAssess = Window(app, title="Assessment Maintenance", width=400,
                   height=400, layout="auto", bg="skyblue3")
frmAssess.hide()
Text(frmAssess, size=24, text="Assessment Maintenance")

studbox = Box(frmAssess, width="fill", align="top", border=True, layout="auto")
_assessments = []
assessList = ListBox(studbox, items=_assessments, height='fill', width='fill',
                     multiselect=False, command=displayAssess, scrollbar=True)
assessList.bg = "cornsilk2"
studbox = Box(frmAssess, width="fill", align="top", border=True, layout="grid")
Text(studbox, text="code:", grid=[0, 0])
Text(studbox, text="Semester:", grid=[0, 1])
Text(studbox, text="year:", grid=[0, 2])
Text(studbox, text="Assess 1:", grid=[0, 3])
Text(studbox, text="Assess 2:", grid=[0, 4])
Text(studbox, text="Assess 3:", grid=[0, 5])

edCrsCode = Text(studbox, text="", width=10, align="left", grid=[1, 0])
edSemester = TextBox(studbox, text="", width=25, align="left", grid=[1, 1])
edYear = TextBox(studbox, text="", width=25, align="left",  grid=[1, 2])
edAssess1 = TextBox(studbox, text="", width=10, align="left",  grid=[1, 3])
edAssess2 = TextBox(studbox, text="", width=10, align="left",  grid=[1, 4])
edAssess3 = TextBox(studbox, text="", width=10, align="left",  grid=[1, 5])

edCrsCode.bg = "skyblue1"
edSemester.bg = "cornsilk2"
edYear.bg = "cornsilk2"
edAssess1.bg = "cornsilk2"
edAssess2.bg = "cornsilk2"
edAssess3.bg = "cornsilk2"

btnbox = Box(frmAssess, width="fill", align="top", border=True, layout="auto")

btn = PushButton(btnbox, text="Update", command=evtUpdateAssess, align="left")
btn.bg = "skyblue1"
btn = PushButton(btnbox, text="Close", command=evtAssessHide, align="left")
btn.bg = "skyblue1"


############# Course maintenance  ##############

## -----local events for Course maintenance ------------ ##

def evtCourseHide():
    frmCourses.hide()


def displayCourses(value):
    global _coursecode

    v = value.split()[0]
    # course code: [description, level, credits, weights[3]]
    if school.courses.validCourse(v):
        m = school.courses.getCourse(v)
        edCode.value = v
        edDesc.value = m[0]
        edLevel.value = m[1]
        edCredits.value = m[2]
        edWeights.value = m[3]
        _coursecode = v


def evtDeleteCourse():
    global _coursecode
    if school.courses.validCourse(_coursecode):
        school.courses.remove(_coursecode)
        refreshLists()
        displayCourses(courseList.items[0])


def evtUpdateCourse():
    global _coursecode

    if school.courses.validCourse(_coursecode):
        m = school.courses.getCourse(_coursecode)
        school.courses.remove(_coursecode)
        school.courses.add(edCode.value, edDesc.value,
                           edLevel.value, edCredits.value, edWeights.value)
        edCode.value = ""
        edDesc.value = ""
        edLevel.value = ""
        edCredits.value = ""
        edWeights.value = ""
        _coursecode = None
        refreshLists()


def evtAddCourse():
    global _coursecode

    if not school.courses.validCourse(_coursecode):
        # assume 30,30,40 default weights for now
        school.courses.add(edCode.value, edDesc.value,
                           edLevel.value, edCredits.value)
        edCode.value = ""
        edDesc.value = ""
        edLevel.value = ""
        edCredits.value = ""
        edWeights.value = ""
        _coursecode = None


## ----- Course form/window ------------ ##
frmCourses = Window(app, title="Course Maintenance", width=450,
                    height=400, layout="auto", bg="skyblue3")
frmCourses.hide()
Text(frmCourses, size=24, text="Course Manager")

corbox0 = Box(frmCourses, width="fill", align="top",
              border=True, layout="auto")
_Courses = []
courseList = ListBox(corbox0, items=_Courses, height='fill', width='fill',
                     multiselect=False, command=displayCourses, scrollbar=True)
courseList.bg = "cornsilk2"
corbox1 = Box(frmCourses, width="fill", align="top",
              border=True, layout="grid")
Text(corbox1, text="Code:", grid=[0, 0])
Text(corbox1, text="Detail:", grid=[0, 1])
Text(corbox1, text="Level:", grid=[0, 2])
Text(corbox1, text="Credits:", grid=[0, 3])
Text(corbox1, text="Weights:", grid=[0, 4])

lvl = [5, 6, 7]
crd = [15, 30, 45, 60]
edCode = TextBox(corbox1, text="", width=20, align="left", grid=[1, 0])
edDesc = TextBox(corbox1, text="", width=50, align="left",  grid=[1, 1])
edLevel = Combo(corbox1,  options=lvl,  align="left", grid=[1, 2])
edCredits = Combo(corbox1,  options=crd,  align="left", grid=[1, 3])
edWeights = TextBox(corbox1, text="", width=25, align="left", grid=[1, 4])

edCode.bg = "cornsilk2"
edDesc.bg = "cornsilk2"
edLevel.bg = "cornsilk2"
edCredits.bg = "cornsilk2"

btnbox1 = Box(frmCourses, width="fill", align="top",
              border=True, layout="auto")
btn = PushButton(btnbox1, text="New", command=evtAddCourse, align="left")
btn.bg = "skyblue1"
btn = PushButton(btnbox1, text="Update",
                 command=evtUpdateCourse,  align="left")
btn.bg = "skyblue1"
btn = PushButton(btnbox1, text="Delete",
                 command=evtDeleteCourse,  align="left")
btn.bg = "skyblue1"
btn = PushButton(btnbox1, text="Cancel", command=evtCourseHide, align="left")
btn.bg = "skyblue1"


############# Main application window ##############

## -----local events for main window ------------ ##

def evtExit():
    """ Confirm quit on exit or close button  """
    # if app.yesno("Close", "Are you sure you want to exit?"):
    exit()


def evtUpdateDetails(value):
    global _studentid
    s = school.findStudentByname(value)
    edTheStudent.value = f"{s.student.studentid} {value}\n{s.student.contact}\n{s.student.email}"

    grades = school.showGradesByid(s.student.studentid)
    edGrades.value = f"- Grades -\n {grades}"
    _studentid = s.student.studentid


def evtFilterRating(rating=None):
    Student_select.clear()
    Course_names = school.findRatedCoursesNames(
        rating) if rating else school.getCourseNames()
    for m in Course_names:
        Student_select.append(m)

# show the student admin dialog box


def evtStudents():
    studentList.clear()
    for s in school.allStudentNames():
        studentList.append(s)
    frmStudent.show(wait=True)

# show the assessment admin dialog box


def evtEnrolments():
    refreshLists()
    frmEnroll.show(wait=True)

# show the assessment admin dialog box


def evtAssessments():
    refreshLists()
    displayAssess(_coursecode)
    frmAssess.show(wait=True)

# show the course admin dialog box


def evtCourses():
    courseList.clear()
    for c in school.courses.courseCodes():
        d = school.courses.getCoursename(c)
        courseList.append(f"{c} - {d}")
    frmCourses.show(wait=True)


def evtLoadDemoData():
    school.clear()
    students = [Student(20220001, "Joe Bloggs", "021-123-1231", "joe.bloggs@mail.com"),
                Student(20220002, "Sue Black", "021-123-1232", "sue.black@mail.com"),
                Student(20220003, "Jane Doe", "021-123-1233", "jane.doe@mail.com"),
                Student(20220004, "Kate White","021-123-1234", "kate.white@mail.com"),
                Student(20220005, "King Kong", "021-123-4567", "king.kong@mail.com")]

    grades = [Grades("CS5100", 1, [50, 50, 50]),
              Grades("PF5110", 1, [60, 60, 60]),
              Grades("CT5120", 1, [70, 70, 70]),
              Grades("WD5130", 1, [80, 80, 80]),
              Grades("UX5210", 1, [65, 65, 65])]

# populate the school with Enrolments
    for s in students:
        e = Enrolment(s, grades)
        school.add(e)

    school.courses.reload()

# refresh all the combo lists
    refreshLists()

## ----- Main window layout------------ ##


Student_names = []
Courses_box = Box(main_box, width="fill", border=3,  layout="grid")
Text(Courses_box, size=24, text="Students", grid=[0, 0])
Text(Courses_box, size=24, text="Student Details", align="left", grid=[1, 0])
edTheStudent = Text(Courses_box, size=16, text="-", align="left", grid=[1, 1])
edTheStudent.text_color = "blue4"
edGrades = Text(Courses_box, size=16, text="", align="left", grid=[1, 2])

Student_select = ListBox(Courses_box, items=Student_names, width=300, height=300,
                         multiselect=False, command=evtUpdateDetails, scrollbar=True, grid=[0, 1, 1, 4])
Student_select.bg = "cornsilk2"
btn_Studentbox = TitleBox(main_box, text="Controls",
                          width="fill", border=3, layout="grid")
btn = PushButton(Courses_box, text="Enrolment",
                 grid=[1, 3], command=evtEnrolments)
btn.bg = "skyblue1"
btn = PushButton(Courses_box, text="Assessments",
                 grid=[2, 3], command=evtAssessments)
btn.bg = "skyblue1"

btn_box = TitleBox(main_box, text="Controls",
                   width="fill", border=3, layout="grid")
btn = PushButton(btn_box, text="Student Admin",
                 grid=[0, 0], command=evtStudents)
btn.bg = "skyblue1"
btn = PushButton(btn_box, text="Course Admin", grid=[1, 0], command=evtCourses)
btn.bg = "skyblue1"
btn = PushButton(btn_box, text="Reload Demo Data",
                 grid=[2, 0], command=evtLoadDemoData)
btn.bg = "skyblue1"
btn = PushButton(btn_box, text="Quit", grid=[3, 0], command=evtExit)
btn.bg = "skyblue1"

evtLoadDemoData()

app.when_closed = evtExit  # confirm exit on X button
app.display()
