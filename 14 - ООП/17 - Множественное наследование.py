class Woman:
    def __init__(self, name):
        self.woman_name = name

    def get_woman_gender(self):
        return 'Woman'

    def get_woman_info(self):
        return f'Name: {self.woman_name}, Gender: {self.get_woman_gender()}'


class Man:
    def __init__(self, name):
        self.man_name = name


    def get_man_gender(self):
        return 'Man'

    def get_man_info(self):
        return f'Name: {self.man_name}, Gender: {self.get_man_gender()}'


class Person(Woman, Man):
    def __init__(self):
        Woman.__init__(self, "Mary")
        Man.__init__(self, "Bary")


c = Person()

print(c.get_man_info())
print(c.get_woman_info())