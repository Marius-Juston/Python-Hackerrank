regex_pattern = r"M{0,3}(?:D?C{0,3}|CD|CM)(?:L?X{0,3}|XL|XC)(?:V?I{0,3}|IV|IX)"


import re

print(str(bool(re.match(regex_pattern, input()))))
