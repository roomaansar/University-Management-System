from university import University
from subjects import Subjects

def main():
    university_management = University(dict({"Umair": ["Power Systems Protection"], "Rooma": ["Introduction To Machine Learning"],
                           "Tayyaba": ["Principles Of Management"]}))
    subjects_registration=Subjects(["Power Systems Protection","Introduction To Machine Learning","Principles Of Management"
                  ,"Electric Machines"])

    while True:
        print("         *** ------------------------------------------------------------------------------------------- ***")
        print("         ***                        Welcome to University Management System                              ***")
        print("         *** ------------------------------------------------------------------------------------------- ***")

        print("What is your current status")
        print("1- Admin \n2- Student")
        status = int(input())
        if status == 1:
            print("What do you want to do?")
            print("1- View Registered Students and their Courses")
            print("2- Delete a student from system")
            print("3- Register a new student on system")
            choice = int(input())
            if choice == 1:
                university_management.registeredStudents()
            elif choice == 2:
                university_management.removeStudent()
            elif choice == 3:
                university_management.registerStudent()
            else:
                print("invalid Choice")




        elif status == 2:
            print("What do you want to do?")
            print("1- View Available Courses")
            print("2- Enroll a Subject")
            print("3- Un-enroll a Subject")
            request=int(input())
            if request == 1:
                subjects_registration.availableCourses()
            elif request == 2:
                university_management.registerStudentSubjects(subjects_registration.enrollCourse())
            elif request==3:
                university_management.unregisterStudentSubjects(subjects_registration.unenrollCourse())
            else:
                print("Invalid Request")


        else:
            exit()

main()