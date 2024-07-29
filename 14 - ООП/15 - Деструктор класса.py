class CourseInfo:

    def __new__(cls, *args, **kwargs):
        print(f"Создание экземпляра курса")

        return super().__new__(cls)

    def __del__(self):
        print(f"Удаление экземпляра курса")

    def __init__(self, course):
        print(f"Инициализация экземпляра курса")

        self.course = course



c = CourseInfo("Python")

del c