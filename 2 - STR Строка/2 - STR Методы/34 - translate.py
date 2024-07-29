course = "python developer 2024"
translation_table = str.maketrans("pd", "PD")
print(translation_table)

print(course.translate(translation_table))


course = "python developer 2024"
translation_table = str.maketrans("pd", "PD", '2024')
print(translation_table)

print(course.translate(translation_table))


course = "python developer 2024"
translation_table = str.maketrans({"p": "P", "4": "5"})
print(translation_table)

print(course.translate(translation_table))


course = "python developer 2024"
translation_table = str.maketrans("","", "2024")
print(translation_table)

print(course.translate(translation_table))