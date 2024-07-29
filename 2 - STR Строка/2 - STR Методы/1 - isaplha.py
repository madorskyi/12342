

course = "Python"

print(course.isalpha())  # True


#region Пустая строка

course = ""

print(course.isalpha())  # False

#endregion

#region Пробел

course = " "

print(course.isalpha())  # True

#endregion

#region Символы

course = "!@#$%^&*()_+"

print(course.isalpha())  # True

#endregion

#region Цифры

course = "2024"

print(course.isalpha())  # True

#endregion

#region Строка с цифрами

course = "Python 2024"

print(course.isalpha())  # True

#endregion

#region Строка с пробелом

course = "Python "

print(course.isalpha())  # True

#endregion