# Примеры строк, которые являются десятичными числами
print("12345".isdecimal())  # True
print("０１２３４５".isdecimal())  # True (широкие символы для цифр)
print("١٢٣٤٥".isdecimal())   # True (арабские цифры)

#region -
print()
#endregion

# Примеры строк, которые не являются десятичными числами
print("123.45".isdecimal())  # False (содержит точку)
print("12345a".isdecimal())  # False (содержит букву)
print("".isdecimal())        # False (пустая строка)
print("Ⅷ".isdecimal())       # False (римская цифра)
