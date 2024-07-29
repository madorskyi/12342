class CourseInfo:

    def __init__(self, course, year):
        self.course_name = course
        self.year = year

    def get_course_info(self):
        return f'{self.course_name}, Year: {self.year}'

    @classmethod
    def custom_course(cls, course, year):
        course = course.title()
        year = int(year) + 1
        return cls(course, year)



user_info = CourseInfo('Python Developer Course', 2024)
print("Course Info:", user_info.get_course_info())


custom_user_info = CourseInfo.custom_course('JavaScript Developer Course', 2024)
print("Custom Course Info:", custom_user_info.get_course_info())
