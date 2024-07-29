

language = "Python"


print(language == "Python")
print(language == "python")

print(language != "Python")
print(language != "python")

print(language > "Python")
print(language > "python")

print(language < "Python")
print(language < "python")

print(language >= "Python")
print(language >= "python")

print(language <= "Python")
print(language <= "python")


    # TODO: Сравнение строк при помощи магических методов: String comparison using magic methods
    #region -
print('\n ---------- Сравнение строк при помощи магических методов: String comparison using magic methods ----------\n')
    #endregion

print(language.__eq__("Python"))
print(language.__eq__("python"))

print(language.__ne__("Python"))
print(language.__ne__("python"))

print(language.__gt__("Python"))
print(language.__gt__("python"))

print(language.__lt__("Python"))
print(language.__lt__("python"))

print(language.__ge__("Python"))
print(language.__ge__("python"))

print(language.__le__("Python"))
print(language.__le__("python"))

