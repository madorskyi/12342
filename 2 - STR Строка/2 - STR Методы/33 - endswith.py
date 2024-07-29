# Примеры, которые возвращают True
print("python".endswith("on"))  # Вывод: True
print("python developer".endswith("developer"))  # Вывод: True
print("PYTHON".endswith("ON"))  # Вывод: True
print("python2024".endswith("2024"))  # Вывод: True
print("python developer 2024".endswith("2024"))  # Вывод: True

# Примеры, которые возвращают False
print("python".endswith("py"))  # Вывод: False
print("python developer".endswith("Python"))  # Вывод: False
print("PYTHON".endswith("on"))  # Вывод: False
print("python2024".endswith("2023"))  # Вывод: False
print("python developer 2024".endswith("developer"))  # Вывод: False

# Примеры с использованием кортежа суффиксов
print("python".endswith(("on", "off")))  # Вывод: True
print("python developer".endswith(("Python", "developer")))  # Вывод: True
print("PYTHON".endswith(("on", "ON")))  # Вывод: True
print("python2024".endswith(("2023", "2024")))  # Вывод: True
print("python developer 2024".endswith(("developer", "2024")))  # Вывод: True

course = "python developer 2024"
print(course.endswith("developer", 0, 17))  # Вывод: True
print(course.endswith("2024", 0, 21))  # Вывод: True
print(course.endswith("python", 0, 6))  # Вывод: True
print(course.endswith("developer", 7, 17))  # Вывод: True
print(course.endswith("2024", 18, 22))  # Вывод: True