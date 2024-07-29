class CourseInfo:

    author = "Madorskyi Roman"

    def __init__(self, course, year):
        self.course = course
        self.year = year


user_info = CourseInfo('Python Developer', 2024)

print('Author:', user_info.author)

print('Author:', CourseInfo.author)

#region -
print()
#endregion

CourseInfo.author = 'New Author'

print('Author after change:', user_info.author)

print('Author:', user_info.author)

#region -
print()
#endregion

user_info.author = 'Madorskyi Roman'

print('Author after change:', CourseInfo.author)

print('Author:', CourseInfo.author)
