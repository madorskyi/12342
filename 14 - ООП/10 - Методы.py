class CourseInfo:

    def __init__(self, course, year):
        self.course_name = course
        self.year = year

    def get_course_info(self):
        return f'Course: {self.course_name}, Year: {self.year}'

    def set_course_info(self, course, year):
        self.course_name = course
        self.year = year


user_info = CourseInfo('Python Developer Course', 2024)
print(user_info.get_course_info())


user_info.set_course_info('JavaScript Developer Course', 2025)
print(user_info.get_course_info())
