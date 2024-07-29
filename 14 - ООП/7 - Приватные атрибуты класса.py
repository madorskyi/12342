class CourseInfo:
    COURSE = 'Python Developer Course'
    AUTHOR = 'ROMAN MADORSKYI'

    def __init__(self, year):
        self._course_name = CourseInfo.COURSE
        self.year = year
        self.__author = CourseInfo.AUTHOR


user_info = CourseInfo(2024)

print('Course: ', user_info._course_name)
print('Year: ', user_info.year)

# AttributeError
# print('Author: ', user_info.__author)