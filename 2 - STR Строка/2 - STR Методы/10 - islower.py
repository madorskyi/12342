#
print("hello".islower())  # Вывод: True
print("hello123".islower())  # Вывод: True
print("hello_world!".islower())  # Вывод: True
print("hello world".islower())  # Вывод: True
print("пайтон разработчик".islower())  # Вывод: True

#region -
print()
#endregion

print("".islower())  # Вывод: False
print("Hello".islower())  # Вывод: False
print("HELLO".islower())  # Вывод: False
print("1234".islower())  # Вывод: False
print(" ".islower())  # Вывод: False