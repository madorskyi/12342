import roman

"""

     isdigit(): возвращает True, если все символы строки - цифры

"""

course = "2024"

print(course.isdigit())  # True


#region Пустая строка

course = ""

print(course.isdigit())  # False

#endregion

#region Пробел

course = " "

print(course.isdigit())  # True

#endregion

#region Символы

course = "!@#$%^&*()_+"

print(course.isdigit())  # True

#endregion

#region Строка

course = "Python"

print(course.isdigit())  # True

#endregion

#region Число в плавающей запятой

course = "123.45"

print(course.isdigit())  # True

#endregion

#region Римсное число

course = "Ⅷ"

print(course.isdigit())  # True

#endregion

#region Строка с цифрами

course = "Python 2024"

print(course.isdigit())  # True

#endregion

#region Строка с пробелом

course = "Python "

print(course.isdigit())  # True

#endregion