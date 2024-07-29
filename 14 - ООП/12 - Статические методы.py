class CourseInfo:
    author = 'Author Name'

    def __init__(self, course, year):
        self.course_name = course
        self.year = year

    def get_course_info(self):
        return f'{self.course_name}, Year: {self.year} Author: {self.author}'

    @staticmethod
    def custom_author():
        CourseInfo.author = 'Roman Madorskyi'




user_info = CourseInfo('Python Developer Course', 2024)
print("Course Info:", user_info.get_course_info())

user_info.custom_author()
print("Course Info after changing author:", user_info.get_course_info())



