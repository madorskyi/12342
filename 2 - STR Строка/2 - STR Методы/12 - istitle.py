# Примеры, где istitle() возвращает True
print("Hello World".istitle())  # True: каждое слово начинается с заглавной буквы
print("Python Programming".istitle())  # True: каждое слово начинается с заглавной буквы
print("This Is A Test".istitle())  # True: каждое слово начинается с заглавной буквы
print("Tabnine Ai".istitle())  # True: каждое слово начинается с заглавной буквы
print("Example String".istitle())  # True: каждое слово начинается с заглавной буквы
print("A B C".istitle())  # True: каждое слово состоит из одной заглавной буквы

# Примеры, где istitle() возвращает False
print("hello world".istitle())  # False: слова начинаются со строчной буквы
print("Python programming".istitle())  # False: второе слово начинается со строчной буквы
print("This is a Test".istitle())  # False: второе и третье слова начинаются со строчной буквы
print("tabnine AI".istitle())  # False: первое слово начинается со строчной буквы, второе слово полностью заглавное
print("example String".istitle())  # False: первое слово начинается со строчной буквы
print("HELLO WORLD".istitle())  # False: все буквы заглавные