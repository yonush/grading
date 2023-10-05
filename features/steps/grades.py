from behave import *

from grade import Grades


@given('an instance of the grades')
def step_impl(context):
    context.grades = Grades()
    assert  isinstance(context.grades,Grades),"an instance of the grades"

@when('the results are [50,50,50]')
def step_impl(context):
    context.grades.assessments = [50,50,50]    
    assert context.grades.assessments == [50,50,50], f"When the results are [50,50,50]"

@then('the grade will be C-')
def step_impl(context):
   assert context.grades.getGrade() == "C-", f"the grade will be C-"

    