import re

regex = r"(?<=.)(#(?:[0-9a-f]{6}|[0-9a-f]{3}))"

for _ in range(int(input())):
    matches = re.finditer(regex, input(), re.MULTILINE | re.IGNORECASE)
    for match in matches:

        for groupNum in range(0, len(match.groups())):
            print(match.group(groupNum))
