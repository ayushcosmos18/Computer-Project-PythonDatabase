import csv
import json
import pandas
from matplotlib import pyplot

def enterMarks(course_id):
    csv_reader = []
    with open("course.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    course_name = ""
    student_marks = {}
    for i in range(1, len(csv_reader)):
        if(csv_reader[i][0] == course_id):
            check = 1
            course_name = csv_reader[i][1]
            student_marks = json.loads(csv_reader[i][2])
            break
    if(check == 0):
        print("Course ID does not exist")
        return
    student_ids = list(student_marks.keys())
    print("Course name: " + course_name)
    for student in student_ids:
        marks = int(input("Enter marks obtained by " + student + ": "))
        student_marks[student] = marks
    df = pandas.read_csv("course.csv")
    df.loc[i - 1, "marks_obtained"] = json.dumps(student_marks)
    df.to_csv("course.csv", index = False)

def viewPerformanceE(course_id):
    csv_reader = []
    with open("course.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    student_marks = {}
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][1] == course_id):
            check = 1
            student_marks = json.loads(csv_reader[i][2])
            break
    if(check == 0):
        print("Course ID does not exist")
        return
    student_ids = list(student_marks.keys())
    for student in student_ids:
        marks = student_marks[student]
        print("Marks obtained by " + str(marks))

