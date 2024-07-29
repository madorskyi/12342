class RubyCourse:

    def get_class_name(self):
        print('Initializing Class RubyCourse')


class PythonCourse(RubyCourse):

    def get_class_name(self):
        print('Initializing Class PythonCourse')


class JavaCourse(RubyCourse):
    def get_class_name(self):
        print('Initializing Class JavaCourse')


class AllCourses(JavaCourse, PythonCourse):

    def get_class_name(self):
        print('Initializing Class AllCourses')


d = AllCourses()
d.get_class_name()


print(AllCourses.__mro__)
print(AllCourses.mro())
help(AllCourses)