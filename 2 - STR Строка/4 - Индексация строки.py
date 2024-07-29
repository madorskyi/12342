course = "Python Developer Course 2024"
print('Length : ', len(course))

#region -
print('---')
#endregion

print(course[7])   # 'D'
print(course[8])   # 'e'
print(course[9])   # 'v'
print(course[10])  # 'e'
print(course[11])  # 'l'
print(course[12])  # 'o'
print(course[13])  # 'p'
print(course[14])  # 'e'
print(course[15])  # 'r'

#region -
print('---')
#endregion

print(course[-21])  # 'D'
print(course[-20])  # 'e'
print(course[-19])  # 'v'
print(course[-18])  # 'e'
print(course[-17])  # 'l'
print(course[-16])  # 'o'
print(course[-15])  # 'p'
print(course[-14])  # 'e'
print(course[-13])  # 'r'



#region ОШИБКИ
print('---')
#endregion

course[0] = "J"
print(course[0])


course = ""
print(course[0])


course = "Python Developer Course 2024"

print(course[2.5])   # TypeError: string indices must be integers
print(course["a"])   # TypeError: string indices must be integers


course = "Python Developer Course 2024"

print(course[30])   # IndexError: string index out of range
print(course[-31])  # IndexError: string index out of range