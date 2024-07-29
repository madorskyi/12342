from collections import defaultdict

data = defaultdict(lambda: "unknown", {"name": "Charlie"})
formatted_string = "My name is {name} and I am {age} years old.".format_map(data)
print(formatted_string)

#region -
print()
#endregion

int_dict = defaultdict(int)
int_dict['a'] += 1
print(int_dict)


list_dict = defaultdict(list)
list_dict['a'].append(1)
list_dict['a'].append(2)
print(list_dict)


str_dict = defaultdict(lambda: "unknown")
str_dict['name'] = "Roman"
print(str_dict['name'])
print(str_dict['age'])