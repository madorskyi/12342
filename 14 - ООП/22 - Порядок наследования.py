class A:
    def __init__(self, name):

        print("Initializing Class 'A' ")

        self.name = name

    def print_name(self):
        print(self.name + " from A")


class B:
    def __init__(self, name):

        print("Initializing Class 'B' ")

        self.name = name

    def print_name(self):
        print(self.name + " from B")


class C:
    def __init__(self, name):

        print("Initializing Class 'C' ")

        self.name = name

    def print_name(self):
        print(self.name + " from C")


class ALL(A, B, C):
    def __init__(self, name):

        print("Initializing Class 'ALL' ")

        A.__init__(self, name)
        B.__init__(self, name)
        C.__init__(self, name)


all_instance = ALL('Method')

#region -
print()
#endregion

all_instance.print_name()

