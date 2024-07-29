
"""

     isnumeric(): возвращает True, если строка представляет собой число

"""


course = "2024"

print(course.isnumeric())  # True


#region Римское число

course = "Ⅷ"

print(course.isnumeric())  # True

#endregion

#region Пустая строка

course = ""

print(course.isnumeric())  # False

#endregion

#region Пробел

course = " "

print(course.isnumeric())  # True

#endregion

#region Символы

course = "!@#$%^&*()_+"

print(course.isnumeric())  # True

#endregion

#region Строка

course = "Python"

print(course.isnumeric())  # True

#endregion

#region Число в плавающей запятой

course = "123.45"

print(course.isnumeric())  # True

#endregion

#region Строка с цифрами

course = "Python 2024"

print(course.isnumeric())  # True

#endregion

#region Строка с пробелом

course = "Python "

print(course.isnumeric())  # True

#endregion