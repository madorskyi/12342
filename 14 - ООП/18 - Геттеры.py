class CourseInfo:
    COURSE = 'Python Developer Course'
    AUTHOR = 'ROMAN MADORSKYI'

    def __init__(self, year):
        self._course_name = CourseInfo.COURSE
        self.year = year
        self.__author = CourseInfo.AUTHOR

    @property
    def author(self):
        return self.__author

    @property
    def course(self):
        return self._course_name

user_info = CourseInfo(2024)


print('Course: ', user_info.course)
print('Author: ', user_info.author)