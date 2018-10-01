import email.utils
import re

n = int(input())

pattern = r'^[a-z][-a-z0-9._]*@[a-z]+\.[a-z]{1,3}$'

for _ in range(n):
    text = input()
    name, email_address = email.utils.parseaddr(text)

    # print(email_address)
    m = re.match(pattern, email_address)
    # print(m)
    if bool(m):
        print(text)
