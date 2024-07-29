class CourseInfo:

    COURSE = 'Python Developer Course'
    AUTHOR = 'ROMAN MADORSKYI'

    def __init__(self,  year):
        self.year = year

user_info = CourseInfo(2024)

print('Course: ', user_info.COURSE)
print('Author: ', user_info.AUTHOR)