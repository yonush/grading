"""
    Online assessment results App: Assessment grading sub-system: database driver code

    Handles the creation of the database and inserting the sample data for
    - students
    - courses
    - grades

    Changelog:
        15JAN2023 - Initial release

"""

import os
import pathlib
import sqlite3
from sqlite3 import Error

# pwd = pathlib.Path().absolute()  # current working folder
conn = None  # databse conenction handle


def dbconnect(db):
    """ 
    Connect to the database
    :param db: databse folder location + datasbe name
    :return conn: database connection handle
    """

    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)
        return None
    return conn


def prepareDB(conn):
    """ 
    Create the database for the website
    :param conn: database connection handle
    :return:
    """

    SQL = ["""
        CREATE TABLE IF NOT EXISTS students (
            id integer PRIMARY KEY,
            name text NOT NULL,
            contact text NOT NULL,
            email text NOT NULL
        );
    """,
           """       
        CREATE TABLE IF NOT EXISTS courses (
            id text PRIMARY KEY,
            name text NOT NULL,
            level integer NOT NULL,
            credits integer NOT NULL,
            weight1 integer NOT NULL,           
            weight2 integer NOT NULL,           
            weight3 integer NOT NULL           
        );           
    """,
           """
        CREATE TABLE IF NOT EXISTS grades (
            id integer PRIMARY KEY,
            studentID integer NOT NULL,
            courseID integer NOT NULL,
            semester integer NOT NULL,            
            assess1 integer NOT NULL,
            assess2 integer NOT NULL,
            assess3 integer NOT NULL,
            year integer NOT NULL                
        );           

    """]
    try:
        for s in SQL:
            db = conn.cursor()
            db.execute(s)
            conn.commit()
    except Error as e:
        print(e)


def importData(conn):
    """ import the sample data into the database
    :param conn: database connection handle
    :return:
    """
    CDATA = [
        ["CS5100", "Computer System Architecture", 5, 15, 30, 30, 40],
        ["PF5110", "Programming Fundamentals", 5, 15, 30, 30, 40],
        ["CT5120", "Concepts & Tools", 5, 15, 30, 30, 40],
        ["WD5130", "Website Development", 5, 15, 30, 30, 40],
        ["UX5210", "UX and UI fundamental", 5, 15, 30, 30, 40],
        ["DT5220", "Intro to Data Concepts", 5, 15, 30, 30, 40],
        ["PM5240", "Agile Projects", 5, 15, 30, 30, 40],
        ["IS5450", "Information Systems", 5, 15, 30, 30, 40],
        ["PR5510", "Intro to OO Programming", 5, 15, 30, 30, 40],
        ["DF6100", "Digital Forensics Fundamentals", 6, 15, 30, 30, 40],
        ["AW6100", "Automation and Embedded Systems", 6, 15, 30, 30, 40],
        ["DB6200", "Database Management Systems", 6, 15, 30, 30, 40],
        ["DC6210", "Data Communications & Networking", 6, 15, 30, 30, 40],
        ["HW6230", "Electronics and Internet of Things Technology", 6, 15, 30, 30, 40],
        ["MA6240", "Maths in IT", 6, 15, 30, 30, 40],
        ["NA6250", "Advanced Networking and the Cloud", 6, 15, 30, 30, 40],
        ["PM6310", "Project Management", 6, 15, 30, 30, 40],
        ["SD6340", "Systems Analysis & Design", 6, 30, 30, 30, 40],
        ["PR6350", "User Experience & User Interfaces", 6, 15, 30, 30, 40],
        ["KM6390", "Knowledge Management", 6, 15, 30, 30, 40],
        ["WD6400", "Adv. Internet and Web Page Development", 6, 15, 30, 30, 40],
        ["PR6500", "Advanced OO Programming", 6, 15, 30, 30, 40],
        ["PR6510", "Enterprise Software Development", 6, 15, 30, 30, 40],
        ["OS6600", "Operating Systems", 6, 15, 30, 30, 40],
        ["AI7110", "Machine Learning and Artificial Intelligence", 7, 15, 30, 30, 40],
        ["FM7120", "Mechatronics in IT", 7, 15, 30, 30, 40],
        ["HW7230", "Enterprise Support and Infrastructure", 7, 15, 30, 30, 40],
        ["DA7240", "Data Analytics", 7, 15, 30, 30, 40],
        ["WD7350", "Web Application Programming", 7, 15, 30, 30, 40],
        ["PJ7390", "Project or Internship", 7, 15, 30, 30, 40],
        ["EC7390", "E-Business Strategies", 7, 15, 30, 30, 40],
        ["ST7400", "Special Topic", 7, 15, 30, 30, 40],
        ["IM7450", "Info Tech Mgmt & Professionalism", 7, 15, 30, 30, 40],
        ["PR7500", "Business Application Programming", 7, 15, 30, 30, 40],
        ["SY7660", "Information Security", 7, 15, 30, 30, 40],
        ["GA7100", "GIS Analytics", 7, 15, 30, 30, 40],
        ["CP7001", "Capstone", 7, 60, 30, 30, 40]
    ]

    SDATA = [
        [20220001, "Joe Bloggs", "021-123-1231", "joe.bloggs@mail.com"],
        [20220002, "Sue Black", "021-123-1232", "sue.black@mail.com"],
        [20220003, "Jane Doe", "021-123-1233", "jane.doe@mail.com"],
        [20220004, "Kate White", "021-123-1234", "kate.white@mail.com"],
        [20220005, "King Kong", "021-123-4567", "king.kong@mail.com"],
    ]

    GDATA = [
        [20220001, "CS5100", 1, 50, 50, 50, 2023],
        [20220001, "PF5110", 1, 60, 60, 60, 2023],
        [20220001, "CT5120", 1, 70, 70, 70, 2023],
        [20220001, "WD5130", 1, 80, 80, 80, 2023],
        [20220001, "UX5210", 1, 65, 65, 65, 2023],

        [20220002, "CS5100", 1, 50, 50, 50, 2023],
        [20220002, "PF5110", 1, 60, 60, 60, 2023],
        [20220002, "CT5120", 1, 70, 70, 70, 2023],
        [20220002, "WD5130", 1, 80, 80, 80, 2023],
        [20220002, "UX5210", 1, 65, 65, 65, 2023],

        [20220003, "CS5100", 1, 50, 50, 50, 2023],
        [20220003, "PF5110", 1, 60, 60, 60, 2023],
        [20220003, "CT5120", 1, 70, 70, 70, 2023],
        [20220003, "WD5130", 1, 80, 80, 80, 2023],
        [20220003, "UX5210", 1, 65, 65, 65, 2023],

        [20220004, "CS5100", 1, 50, 50, 50, 2023],
        [20220004, "PF5110", 1, 60, 60, 60, 2023],
        [20220004, "CT5120", 1, 70, 70, 70, 2023],
        [20220004, "WD5130", 1, 80, 80, 80, 2023],
        [20220004, "UX5210", 1, 65, 65, 65, 2023],

        [20220005, "CS5100", 1, 50, 50, 50, 2023],
        [20220005, "PF5110", 1, 60, 60, 60, 2023],
        [20220005, "CT5120", 1, 70, 70, 70, 2023],
        [20220005, "WD5130", 1, 80, 80, 80, 2023],
        [20220005, "UX5210", 1, 65, 65, 65, 2023],
    ]

    cur = conn.cursor()
    # import the courses
    for d in CDATA:
        print(d)
        cur.execute("INSERT INTO courses (id,name,level,credits,weight1,weight2,weight3) VALUES(?,?,?,?,?,?,?)",
                    (d[0], d[1], d[2], d[3], d[4], d[5], d[6]))
    conn.commit()

    # import the students
    for d in SDATA:
        print(d)
        cur.execute(
            "INSERT INTO students (id,name,contact,email) VALUES(?,?,?,?)", (d[0], d[1], d[2], d[3]))
    conn.commit()

    # import the grades
    i = 0
    for d in GDATA:
        print(d)
        i += 1
        cur.execute("INSERT INTO grades (id,studentID,courseID,semester,assess1,assess2,assess3,year) VALUES(?,?,?,?,?,?,?,?)",
                    (i, d[0], d[1], d[2], d[3], d[4], d[5], d[6]))
    conn.commit()

    cur.close()


if __name__ == "__main__":
    db = os.getcwd()+"\\school.db"
    print(f"Import data into {db}")
    if "school.db" in os.listdir():
        print("- Removing existing database")
        os.remove(db)

    conn = dbconnect(db)
    if conn:
        print("- creating tables")
        prepareDB(conn)
        print("- importing data")
        importData(conn)
    conn.close()
    print("Import complete")
