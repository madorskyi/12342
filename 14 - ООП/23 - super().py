#region -

# class RubyCourse:
#     def __init__(self, name):
#         print('Initializing Class RubyCourse')
#
#
# class PythonCourse(RubyCourse):
#     def __init__(self, name):
#         print('Initializing Class PythonCourse')
#
#
# class JavaCourse(RubyCourse):
#     def __init__(self, name):
#         print('Initializing Class JavaCourse')
#
#
# class AllCourses(PythonCourse, JavaCourse):
#     def __init__(self, name):
#
#         PythonCourse.__init__(self, name)
#         JavaCourse.__init__(self, name)
#         RubyCourse.__init__(self, name)
#
#         print('Initializing Class AllCourses')
#
#
# all_courses = AllCourses('All Courses')

#endregion

# region -

class RubyCourse:
    def __init__(self, name):
        print('Initializing Class RubyCourse')


class PythonCourse(RubyCourse):
    def __init__(self, name):
        RubyCourse.__init__(self, name)
        print('Initializing Class PythonCourse')


class JavaCourse(RubyCourse):
    def __init__(self, name):
        RubyCourse.__init__(self, name)
        print('Initializing Class JavaCourse')


class AllCourses(PythonCourse, JavaCourse):
    def __init__(self, name):

        PythonCourse.__init__(self, name)
        JavaCourse.__init__(self, name)

        print('Initializing Class AllCourses')


all_courses = AllCourses('All Courses')

#endregion


class RubyCourse:
    def __init__(self, name):
        print('Initializing Class RubyCourse')

class PythonCourse(RubyCourse):
    def __init__(self, name):
        super().__init__(name)

        print('Initializing Class PythonCourse')


class JavaCourse(RubyCourse):
    def __init__(self, name):
        super().__init__(name)

        print('Initializing Class JavaCourse')


class AllCourses(PythonCourse, JavaCourse):
    def __init__(self, name):
        super().__init__(name)

        print('Initializing Class AllCourses')


all_courses = AllCourses('All Courses')
