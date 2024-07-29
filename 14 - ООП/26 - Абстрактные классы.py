from abc import ABC


class User(ABC):

    def __init__(self):
        super().__init__()
        print('Initializing User')


class Student(User):

    def __init__(self):
        super().__init__()
        print('Initializing Student')

c = Student()
