formatted_string = "|{:<10}|{:^10}|{:>10}|".format("left", "center", "right")
print(formatted_string)


pi = 3.14159
formatted_string = "The value of pi is approximately {:.2f}".format(pi)
print(formatted_string)


course = "Python Developer Course"
year = 2024
formatted_string = "This {} was created in {}.".format(course, year)
print(formatted_string)


course = "Python Developer Course"
year = 2024
formatted_string = "This {0} was created in {1}.".format(course, year)
print(formatted_string)


formatted_string = "This {course} was created in {year}.".format(course="Python Developer Course", year='2024')
print(formatted_string)