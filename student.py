"""
    Student Class

    Handles students pesonal info

    Changelog:
        10JAN2023 - Initial release

"""


class Student:
    # Constructor
    def __init__(self, studentid=None, name="", contact="", email=""):
        self._studentid = studentid
        self._name = name
        self._contact = contact
        self._email = email

    @property
    def studentid(self):
        return int(self._studentid)

    @studentid.setter
    def studentid(self, studentid):
        if not studentid:
            raise ValueError

        if len(str(studentid)) != 8:
            raise ValueError
        try:
            studentid = int(studentid)
        except:
            raise ValueError
        self._studentid = studentid
        return self

    # Public methods
    def get_student(self):
        return self.name

    @property
    def name(self):
        return str(self._name)

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError
        self._name = name
        return self

    @property
    def email(self):
        return str(self._email)

    @email.setter
    def email(self, email):
        if not email:
            raise ValueError
        self._email = email
        return self

    @property
    def contact(self):
        return str(self._contact)

    @contact.setter
    def contact(self, contact):
        if not contact:
            raise ValueError
        self._contact = contact
        return self

    def show(self):
        return "\n".join([f"Student ID: {self.studentid}",
                          f"Student: {self._name}",
                          f"Contact: {self._contact}",
                          f"Email: {self._email}", ])

    def __str__(self):
        return self.show()


# End of class, tests below
if __name__ == "__main__":
    print("Start Tests")
    c = Student(20220001, "Joe Bloggs", "021-123-1234", "joe.bloggs@mail.com")
    print(c)
    assert str(c) == "Student ID: 20220001\nStudent: Joe Bloggs\nContact: 021-123-1234\nEmail: joe.bloggs@mail.com", \
        "__str__ not the same"

    assert c.show() == "Student ID: 20220001\nStudent: Joe Bloggs\nContact: 021-123-1234\nEmail: joe.bloggs@mail.com", \
        "show not the same"

    print(c.email)
    c.email = "joe@gmail.com"
    print(c.email)
    assert c.email == "joe@gmail.com", "Basic Setters and show"

    try:
        c.studentid = 202212345
    except ValueError:
        pass
    except:
        raise

    # FIXME: Tests for class methods

    print("End Tests")
