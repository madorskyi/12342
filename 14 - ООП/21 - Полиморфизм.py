class JavaCourse:

    def get_course_info(self):
        return "Java Course"


class PythonCourse:

    def get_course_info(self):
        return "Python Course"


class JSCourse:

    def get_course_info(self):
        return "JavaScript Course"



python_course = PythonCourse()
java_course = JavaCourse()
js_course = JSCourse()

for i in [python_course, java_course, js_course]:
    print(i.get_course_info())