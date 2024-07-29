course = 'Python Developer Course'
print('Length : ', len(course))

#region -
print('---')
#endregion

my_slice = slice(None)
print(course[my_slice])

my_slice = slice(6)
print(course[my_slice])

my_slice = slice(7, None)
print(course[my_slice])

my_slice = slice(7, 16)
print(course[my_slice])

my_slice = slice(-6, None)
print(course[my_slice])

my_slice = slice(None, -7)
print(course[my_slice])

my_slice = slice(-16, -8)
print(course[my_slice])

my_slice = slice(-18, None, -1)
print(course[my_slice])

my_slice = slice(-1, -7, -1)
print(course[my_slice])