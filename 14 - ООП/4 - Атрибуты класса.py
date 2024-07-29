class CourseInfo:

    author = "Madorskyi Roman"

    def __init__(self, course, year):
        self.course = course
        self.year = year


print('Class Attributes: ', CourseInfo.__dict__)


user_info = CourseInfo('Python Developer', 2024)


print('Author object:', user_info.author)

print('Author class:', CourseInfo.author)

#region -
print()
#endregion
