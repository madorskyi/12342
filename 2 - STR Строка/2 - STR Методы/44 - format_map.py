# Пример 1: Простое форматирование с использованием словаря
user_info = {"name": "Roman", "age": 27}
formatted_string = "My name is {name} and I am {age} years old.".format_map(user_info)
print(formatted_string)


user_info = {"name": "Roman", "age": 27, "city": "Tel Aviv"}
formatted_string = "My name is {name}, I am {age} years old and I live in {city}.".format_map(user_info)
print(formatted_string)



from collections import defaultdict

data = defaultdict(lambda: "unknown", {"name": "Charlie"})
formatted_string = "My name is {name} and I am {age} years old.".format_map(data)
print(formatted_string)

