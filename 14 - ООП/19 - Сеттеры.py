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

    @course.setter
    def course(self, new_course):
        self._course_name = new_course


    @author.setter
    def author(self, new_author):
        self.__author = new_author


user_info = CourseInfo(2024)

print('Course before change: ', user_info.course)
print('Author before change: ', user_info.author)

#region -
print()
#endregion

user_info.course = 'Python Developer Course - Updated'
user_info.author = 'NEW AUTHOR'

print('Course after change:', user_info.course)
print('Author after change:', user_info.author)