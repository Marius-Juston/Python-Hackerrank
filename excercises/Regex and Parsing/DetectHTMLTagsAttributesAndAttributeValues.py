import re

text = ''

comment = re.compile('<!--.+?-->')

for _ in range(int(input())):
    text += input()

text = comment.sub('', text)

html_stuff = re.compile(r'<(\w+)(.*?)/?>')
data = re.compile(r'([a-z-])="([^"]+)')

for groups in html_stuff.finditer(text):
    groups: re.Match

    print(groups.group(1))

    for info in data.finditer(groups.group(2)):
        print("->", info.group(1), ">", info.group(2))
