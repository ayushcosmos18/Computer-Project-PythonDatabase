while(True):
    print("For student operations press 1")
    print("For course operations press 2")
    print("For batch operations press 3")
    print("For department operations press 4")
    print("For examination operations press 5")
    print("Press 0 to stop")
    x = int(input("Enter your choice: "))
    if(x == 0):
        break
    elif(x == 1):
        from student import *
        while(True):
            print("To create a student Press 1")
            print("To update a student's details Press 2")
            print("To remove a student Press 3")
            print("To generate report card of a student Press 4")
            print("To return to main menu press 0")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                student_id = input("Enter student ID: ")
                student_name = input("Enter student name: ")
                createStudent(student_id, student_name)
            elif(y == 2):
                ostudent_id = input("Enter old student ID: ")
                updateStudent(ostudent_id)
            elif(y == 3):
                student_id = input("Enter student ID: ")
                removeStudent(student_id)
            elif(y == 4):
                student_id = input("Enter student ID: ")
                reportCard(student_id)
            else:
                print("Invalid input. Try again.")  
    elif(x == 2):
        from course import *
        while(True):
            print("To create a course Press 1")
            print("To view performance of students on course Press 2")
            print("To show course statistics as histogram Press 3")
            print("To return to main menu Press 0")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                course_id = input("Enter course ID: ")
                course_name = input("Enter course name: ")
                createCourse(course_id, course_name)
            elif(y == 2):
                course_id = input("Enter course ID: ")
                checkPerformance(course_id)
            elif(y == 3):
                course_id = input("Enter course ID: ")
                courseStatistics(course_id)
            else:
                print("Invalid input. Try again.")
    elif(x == 3):
        from batch import *
        while(True):
            print("To create a batch Press 1")
            print("To view all students in a batch Press 2")
            print("To show all courses in a batch Press 3")
            print("To view performance of all students in a batch Press 4")
           
            print("To return to main menu Press 0")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                batch_name = input("Enter batch name: ")
                createBatch(batch_name)
            elif(y == 2):
                batch_id = input("Enter batch ID: ")
                viewStudents(batch_id)
            elif(y == 3):
                batch_id = input("Enter batch ID: ")
                viewCourses(batch_id)
            elif(y == 4):
                batch_id = input("Enter batch ID: ")
                viewPerformance(batch_id)
            
            else:
                print("Invalid input. Try again.")
    elif(x == 4):
        from department import *
        while(True):
            print("To create a department Press 1")
            print("To view all batches in a department Press 2")
            print("To view average performance of all betches in a department Press 3")
            print("To return to main menu Press 0")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                department_id = input("Enter department ID: ")
                department_name = input("Enter department name: ")
                createDepartment(department_id, department_name)
            elif(y == 2):
                department_id = input("Enter department ID: ")
                viewBatches(department_id)
            elif(y == 3):
                department_id = input("Enter department ID: ")
                viewPerformanceD(department_id)
            else:
                print("Invalid input. Try again.")
    elif(x == 5):
        from examination import *
        while(True):
            print("To enter marks of all students for an exam Press 1")
            print("To view performance of all students in an exam Press 2")
            print("To return to main menu press 0")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                course_id = input("Enter course ID: ")
                enterMarks(course_id)
            elif(y == 2):
                course_id = input("Enter course ID: ")
                viewPerformanceE(course_id)
            else:
                print("Invalid input. Try again.")
    else:
        print("Invalid input. Try again.")
