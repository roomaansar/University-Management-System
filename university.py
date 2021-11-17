class University:
    def __init__(self, registered_students):
        self.registered_students_list = registered_students

    # display registered students and their courses
    def registeredStudents(self):
        for student, courses in self.registered_students_list.items():
            print(student + ": " + str(courses))

    # enter a new student into system
    def registerStudent(self):
        new_student = input("Name of student: ").title()
        if new_student.title() in self.registered_students_list:
            print(new_student + " is already registered")
        else:
            self.registered_students_list[new_student] = []

    # process the course enroll request from a student
    def registerStudentSubjects(self, course):
        student_name=input("Student's name: ").title()
        for students, courses in self.registered_students_list.items():
            if student_name in students:
                if course not in self.registered_students_list[student_name]:
                    self.registered_students_list[student_name].append(course)
                    print("Enroling was successful")

    # process the course un-enroll request from a student
    def unregisterStudentSubjects(self, course):
        student_name=input("Student's name: ")
        for students, courses in self.registered_students_list.items():
            if student_name in students:
                if course in self.registered_students_list[student_name]:
                    self.registered_students_list[student_name].remove(course)
                    print("Unenrolling was successful")
                else:
                    print("No such course was enrolled under this student's name")

    # remove a student from system
    def removeStudent(self):
        delstudt = input("Enter the name of student you want to delete from student directory: ")
        if delstudt in self.registered_students_list:
            del self.registered_students_list[delstudt]
