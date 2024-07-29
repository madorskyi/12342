class A:
    def __init__(self):
        print("Инициализация класса A")
        self.value = 5

    def __str__(self):
        return f"A с значением {self.value}"

    def __del__(self):
        print("Удаление экземпляра класса A")

    def __repr__(self):
        return f"A(value={self.value})"


print(dir(A))

