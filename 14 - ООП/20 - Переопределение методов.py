class Course:
    AUTHOR = 'ROMAN MADORSKYI'

    def __init__(self, course_name, course_year):
        self.course_name = course_name
        self.course_year = course_year

    def get_author(self):
        return f'Course Author: {Course.AUTHOR}'

    def get_course_language(self):
        return f'Course name: {self.course_name}'

    def get_course_year(self):
        return f'Course year: {self.course_year}'


class CourseInfo(Course):

    def __init__(self):
        Course.__init__(self, 'Python Developer Course', 2024)


    def get_course_info(self):
        return f'Course name: {self.course_name}\nCourse Author: {self.AUTHOR}\nCourse year: {self.course_year}'

    def get_author(self):

        print('Overriding the method to print author in title case')

        return f'Course Author: {Course.AUTHOR.title()}'



a = CourseInfo()

print('Class name: ', type(a).__name__)

print(a.get_author())