# Примеры строк, которые являются ASCII
print("Hello".isascii())  # True
print("12345".isascii())  # True
print("!@#$%".isascii())  # True
print("".isascii())       # True (пустая строка)
print("\n\t\r".isascii())  # True

#region -
print()
#endregion

# Примеры строк, которые не являются ASCII
print("Привет".isascii())  # False (кириллица)
print("你好".isascii())     # False (китайские иероглифы)
print("こんにちは".isascii()) # False (японские символы)
print("Hello 😊".isascii())  # False
print("０１２３４５".isascii())  # False
