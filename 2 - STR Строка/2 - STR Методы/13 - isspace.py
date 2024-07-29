# Примеры, где isspace() возвращает True
print("   ".isspace())
print("\t".isspace())
print("\n".isspace())
print("\r".isspace())
print("\f".isspace())
print("\v".isspace())

# Примеры, где isspace() возвращает False
print("".isspace())
print("hello world".isspace())
print("  hello  ".isspace())
print("123".isspace())
print("!@#".isspace())
print("word\t\t\t".isspace())