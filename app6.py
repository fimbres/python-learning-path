import re

patron = re.compile(r'\bIsaac\b')
value = "Isaac Isaac"
data = patron.findall(value)
print(data)

