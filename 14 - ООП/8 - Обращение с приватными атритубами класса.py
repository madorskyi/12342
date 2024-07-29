class CourseInfo:

    def __init__(self, course, year, author):
        self._course_name = course
        self.__author = author
        self.year = year


user_info = CourseInfo('Python Developer Course', 2024, 'ROMAN POMIDORSKYI')


print('Course: ', user_info._course_name)
print('Year: ', user_info.year)


# AttributeError
# print('Author: ', user_info.__author)


print(user_info._CourseInfo__author)
user_info._CourseInfo__author = 'ROMAN MADORSKYI'

print(user_info._CourseInfo__author)


print(getattr(user_info, '_CourseInfo__author'))

print(hasattr(user_info, '_CourseInfo__author'))

setattr(user_info, '_CourseInfo__author', 'NEW AUTHOR')

delattr(user_info, '_CourseInfo__author')
