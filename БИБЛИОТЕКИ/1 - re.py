import re

course = "Python, Developoer; Course: 2024"
print(re.split('[,;:]', course))


course = "Python, Developoer; Course: 2024"
print(re.split('[,; ]', course))