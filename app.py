"""
    Online assessment sub-system

    Handles students assessments for a selected course over the Internet

    Changelog:
        28NOV2022 - Initial release

    This requires the Flask module
    pip install flask
"""

import os
import sqlite3
from sqlite3 import Error

from flask import Flask, redirect, render_template, request
from flask.helpers import flash, url_for

import schooldb

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"


@app.route("/")
def main():
    """
    Route for home/index.html
    :param:
    :return:
    """
    return render_template("index.html")


@app.route("/grade/<int:grade_id>/edit", methods=["POST", "GET"])
def edit_grade(grade_id):
    """
    Route for editing a single grade /grade/#/edit
    :param:
    :return:
    """

    conn = sqlite3.connect("school.db")
    cur = conn.cursor()

    """
    To prevent "sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 2 supplied"
        # https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
        bindgings should be a tuple
        (str(grade_id)) versus (str(grade_id),) - note the extra comma at the end
    """
    grade = cur.execute(
        "SELECT id, studentID, courseID, assess1, assess2, assess3, semester FROM grades WHERE id=?",
        (str(grade_id),),
    ).fetchone()
    student_id = grade[1]
    if request.method.upper() == "POST":
        assess1 = request.form.get("assess1")
        assess2 = request.form.get("assess2")
        assess3 = request.form.get("assess3")

        if (
            assess1 == None
            or assess2 == None
            or assess3 == None
            or assess1.strip() == ""
            or assess2.strip() == ""
            or assess3.strip() == ""
        ):
            flash("Please fill in all of the fields")
            return render_template("edit.html", grade=grade)

        SQL = "UPDATE grades SET assess1 = ?, assess2 = ?, assess3 = ? WHERE id = ?"
        cur.execute(SQL, (assess1, assess2, assess3, grade_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("display_grades", student_id=student_id))
    cur.close()
    conn.close()
    return render_template("edit.html", grade=grade)


@app.route("/grade/<int:grade_id>/delete")
def delete_grade(grade_id):
    """
    Route for removing a single grade /grade/#/delete
    :param:
    :return:
    """
    student_id = request.args["student_id"]
    conn = sqlite3.connect("school.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM grades WHERE grades.id = ?", (str(grade_id),))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for("display_grades", student_id=student_id))


# students: id, name, contact, email
# grades: id, studentID, courseID, assess1, assess2, assess3, semester
# courses: id, name, level, credits, weight1, weight2, weight3


@app.route("/grades/<int:student_id>/")
def display_grades(student_id):
    """
    Route for showing the grades of a single student /grades/#
    :param:
    :return:
    """
    conn = sqlite3.connect("school.db")
    cur = conn.cursor()
    SQL = """
        SELECT studentID, courseID, assess1, assess2, assess3, semester, grades.id
        FROM grades,students 
        WHERE grades.studentID = students.id 
        AND students.id=?
    """
    # grades = cur.execute(SQL, (str(student_id))).fetchone()
    # Without the comma, (student_id) is just a grouped expression, not a tuple,
    # and thus the img string is treated as the input sequence.
    cur.execute(SQL, (str(student_id),))
    grades = cur.fetchall()

    return render_template("grades.html", grades=grades, student_id=student_id)


@app.route("/students")
def display_students():
    """
    Route for listing all of the students /students
    :param:
    :return:
    """

    conn = sqlite3.connect("school.db")
    cur = conn.cursor()
    SQL = """
        SELECT id, name, email
        FROM students
    """
    cur.execute(SQL)
    students = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("students.html", students=students)


# driver code for the flask application
if __name__ == "__main__":
    conn = None
    db = os.getcwd() + "\\school.db"
    if "school.db" not in os.listdir():
        conn = schooldb.dbconnect(db)
        if conn:
            schooldb.prepareDB(conn)
            schooldb.importData(conn)
    if conn:
        conn.close()
    app.run(debug=True)
