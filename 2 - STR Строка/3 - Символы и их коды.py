char = 'A'
print('Type : ', type(char))
print('Value : ', char)

#region -
print('---')
#endregion

print('ord : ', ord(char))
print('chr : ', chr(ord(char)))

#region -
print()
#endregion

char = 'B'
print('ord : ', ord(char))
print('chr : ', chr(ord(char)))

#region -
print()
#endregion

char = 'C'
print('ord : ', ord(char))
print('chr : ', chr(ord(char)))

#region -
print()
#endregion

char = '😊'
print('ord : ', ord(char))
print('chr : ', chr(ord(char)))

#region -
print()
#endregion

char = '字'
print('ord : ', ord(char))
print('chr : ', chr(ord(char)))


#region ОШИБКИ
print('---')
#endregion

# chr(-1)         # ValueError
# chr(1114112)    # ValueError
# ord('AB')       #TypeError