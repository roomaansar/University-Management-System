class Subjects():
    def __init__(self,available_courses):
        self.available_courses_list=available_courses

    # display available courses
    def availableCourses(self):
        for course in self.available_courses_list:
           print(course)

    # opportunity for student to enroll in a subject
    def enrollCourse(self):
        course_to_register=input("Enter course name you want to be enrolled in:").title()
        if course_to_register in self.available_courses_list:
            self.course = course_to_register
            return self.course
        else:
            print("Course not available")


    # opportunity for student to un-enroll from a subject
    def unenrollCourse(self):
        course = input("Which course you want to unregister?").title()
        if course in self.available_courses_list:
            self.course=course
            return self.course

