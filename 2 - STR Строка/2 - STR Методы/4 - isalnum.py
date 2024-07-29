

print("abc123".isalnum())  # True
print("ABC123".isalnum())  # True
print("123456".isalnum())  # True
print("abcABC".isalnum())  # True


# Примеры строк с символами других алфавитов
print("абв123".isalnum())   # True (кириллица и цифры)
print("你好123".isalnum())   # True (китайские иероглифы и цифры)
print("こんにちは".isalnum()) # True (японские символы)


# Примеры строк, которые не являются буквенно-цифровыми
print("abc 123".isalnum())  # False (содержит пробел)
print("abc-123".isalnum())  # False (содержит дефис)
print("abc!".isalnum())     # False (содержит восклицательный знак)
print("".isalnum())         # False (пустая строка)