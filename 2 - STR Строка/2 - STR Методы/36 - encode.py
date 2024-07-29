course = "Python Developer 2024"
print(course.encode('utf-8'))

course = "Python Developer 2024"
print(course.encode('utf-16'))

course = "Python Developer 2024"
print(course.encode('ascii'))

course = "Python Developer 2024😊"
print(course.encode('ascii','ignore'))


course = "Python курс!"
print(course.encode("ascii", errors="ignore"))

course = "Python курс!"
print(course.encode("ascii", errors="replace"))